from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import requests
import json
from django.http import HttpResponse
from rest_framework.parsers import BaseParser
from .serializers import bkashOnboardingSerializer


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
    serializer_class = bkashOnboardingSerializer

    def post(self, request):
        # url = "http://rdp.bracnet.net/rdp_client_invoices/rdp_customer_bill_generation_auto.php"
        # payload = {"transaction_id": "798b97e6-1232-4e4f-8422-c97befc6357d",
        #            "customer_id": 11002,
        #            "store_amount": 800,
        #            "payment_method": 9}
        # headers = {"Content-Type": "application/json; charset=utf-8"}
        # res = requests.post(url, data=json.dumps(payload), headers=headers)
        # response = HttpResponse(request, content_type="text/plain")
        plain_text = request.data.decode('utf-8')

        plain_text_split = str(plain_text).split('{')
        plain_text_split = "{" + plain_text_split[1]
        data_dict = {"onbording_res": json.loads(plain_text_split)}
        serializer = self.serializer_class(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(json.loads(plain_text_split))
