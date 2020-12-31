from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import requests
import json


class BkashWebhookApiView(GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        url = "http://rdp.bracnet.net/rdp_client_invoices/rdp_customer_bill_generation_auto.php"
        payload = {"transaction_id": "798b97e6-1232-4e4f-8422-c97befc6357d",
                   "customer_id": 11002,
                   "store_amount": 800,
                   "payment_method": 9}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        res = requests.post(url, data=json.dumps(payload), headers=headers)
        python_obj = json.loads(request.data)
        print(python_obj)
        return Response(request.data)
