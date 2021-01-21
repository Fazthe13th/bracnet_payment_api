from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import requests
import json
from django.http import HttpResponse
from rest_framework.parsers import BaseParser
from .serializers import bkashWebhookSerializer, bkashOnboardingSerializer
import datetime


class PlainTextParser(BaseParser):
    """Custom plain text parser to extract 'text/plain' payloads from requests."""

    media_type = 'text/plain'
    format = 'text'

    def parse(self, stream, media_type=None, parser_context=None):
        """Simply returns a string representing the body of the request.

        Args:
            stream (bytes): A stream-like object representing the body of the request.
            media_type (str): Default 'Content-type' of the request.
            parser_context(dict): Dictionary containing any additional context that is required to parse the content.

        Returns:
            `data`: will simply be a string representing the body of the request.
            `files`: will always be `None`.
        """
        return stream.read()
        # try:

        # except ValueError as error:
        #     raise exceptions.ValidationError(
        #         'Text-plain parse error - %s' % error)


class BkashWebhookApiView(GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    parser_classes = [PlainTextParser]
    serializer_class = bkashWebhookSerializer

    def datetime_format(self, date_time_str):
        if date_time_str:
            year = date_time_str[:4]
            month = date_time_str[4:6]
            day = date_time_str[6:8]
            hour = date_time_str[8:10]
            minute = date_time_str[10:12]
            second = date_time_str[12:14]
            contacted_date = year + "-" + month + "-" + \
                day + " " + hour + ":" + minute + ":" + second
            date_time_obj = datetime.datetime.strptime(
                contacted_date, '%Y-%m-%d %H:%M:%S')
            return date_time_obj
        else:
            return None

    def post(self, request):
        plain_text = request.data.decode('utf-8')
        sep = '{'
        extract_json = plain_text[plain_text.index(sep):]
        converted_json = json.loads(extract_json)
        if converted_json["Type"] == 'SubscriptionConfirmation' or converted_json['Type'] == 'UnsubscribeConfirmation':
            data_dict = {
                "onbording_res": converted_json
            }
            confirmation_msg = bkashOnboardingSerializer(
                data=data_dict)
            confirmation_msg.is_valid(raise_exception=True)
            confirmation_msg.save()
        if converted_json["Type"] == 'Notification':
            bKash_message = json.loads(str(converted_json["Message"]))
            format_datetime = self.datetime_format(
                bKash_message.get('dateTime', None))
            data_dict = {
                "sns_response": converted_json,
                "transaction_id": bKash_message.get('trxID', ),
                "transaction_datetime": format_datetime,
                "payment_from": bKash_message['debitMSISDN'],
                "transaction_status": bKash_message['transactionStatus'],
                "transaction_reference": bKash_message.get('transactionReference', None),
                "amount": "{:.2f}".format(float(bKash_message['amount'])),
                "currency": bKash_message['currency']
            }

            serializer = self.serializer_class(data=data_dict)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if data_dict['transaction_reference'] and str(data_dict['transaction_reference']).isdigit():
                url = "http://rdp.bracnet.net/rdp_client_invoices/rdp_customer_bill_generation_auto.php"
                payload = {"transaction_id": data_dict['transaction_id'],
                           "customer_id": data_dict['transaction_reference'],
                           "payment_number": data_dict['payment_from'],
                           "store_amount": data_dict['amount'],
                           "payment_method": 7}
                headers = {"Content-Type": "application/json; charset=utf-8"}
                requests.post(url, data=json.dumps(payload), headers=headers)
            # if not data_dict['transaction_reference']:
            #     url = "http://rdp.bracnet.net/rdp_client_invoices/rdp_customer_bill_generation_auto.php"
            #     payload = {"transaction_id": data_dict['transaction_id'],"customer_id": None,
            #                "payment_number": data_dict['payment_from'],
            #                "store_amount": data_dict['amount'],
            #                "payment_method": 7}
            #     headers = {"Content-Type": "application/json; charset=utf-8"}
            #     requests.post(url, data=json.dumps(payload), headers=headers)
        return Response(converted_json)
