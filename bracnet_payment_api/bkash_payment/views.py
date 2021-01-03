from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import requests
import json
from django.http import HttpResponse
from rest_framework.parsers import BaseParser


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()


class BkashWebhookApiView(GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    parser_classes = [PlainTextParser]

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
        print(plain_text)
        return Response(plain_text)
