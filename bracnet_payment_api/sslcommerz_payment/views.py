from .models import SslcommerzPaymentInitializationModel
from .serializers import SslcommerzPaymentInitializationSerializer, SslcommerzIPNSerializer, SslcommerzValidationSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.db import DatabaseError, DataError
from django.shortcuts import redirect
from rest_framework.reverse import reverse
from . SslcommerzAPICall.sslcommerz import SSLCommerzfunc
import uuid
import os


class SslcommerzPaymentInitializationView(ListCreateAPIView):
    serializer_class = SslcommerzPaymentInitializationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SslcommerzPaymentInitializationModel.objects.all()
    sslc_tran_uuid = uuid.uuid4()
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        serializer = SslcommerzPaymentInitializationSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            post_body = {
                'tran_id': self.sslc_tran_uuid,
                'total_amount': self.request.data['total_amount'],
                'currency': self.request.data['currency'],
                'success_url': str(os.getenv("SUCCESS_URL_SSLC")),
                'fail_url': str(os.getenv("SUCCESS_URL_SSLC")),
                'cancel_url': str(os.getenv("SUCCESS_URL_SSLC")),
                'emi_option': self.request.data['emi_option'],
                'cus_name': self.request.data['cus_name'],
                'cus_email': self.request.data['cus_email'],
                'cus_phone': self.request.data['cus_phone'],
                'cus_add1': self.request.data['cus_add1'],
                'cus_city': self.request.data['cus_city'],
                'cus_country': self.request.data['cus_country'],
                'shipping_method': self.request.data['shipping_method'],
                'num_of_item': self.request.data['num_of_item'],
                'product_name': self.request.data['product_name'],
                'product_category': self.request.data['product_category'],
                'product_profile': self.request.data['product_profile']
            }
            self.sslc_response = self.SSLCommerz.create_session(post_body)
            if self.sslc_response['status'] == 'FAILED':
                serializer.save(tran_id=self.sslc_tran_uuid,
                                status=self.sslc_response['status'], failed_reason=self.sslc_response['failedreason'])
                return Response({'error': 'SSLCommerz session creation failed',
                                 'failed_reason': self.sslc_response['failedreason']}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer.save(tran_id=self.sslc_tran_uuid,
                            status=self.sslc_response['status'], failed_reason=self.sslc_response['failedreason'])
            return Response({'msg': 'SSLCommerz session created',
                             'payment_url': self.sslc_response['GatewayPageURL']}, status=status.HTTP_200_OK)
        except DatabaseError:
            return Response({'error': 'Database error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SSLCommerzIPNView(GenericAPIView):
    serializer_class = SslcommerzIPNSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            validate_url = reverse('sslc_payment_validate', request=request)
            return redirect(validate_url)
        except Exception:
            return Response({'msg': 'SSLCommarz IPN response parsing failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SSLCommerzValidateView(ListCreateAPIView):
    serializer_class = SslcommerzValidationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # post_body = {
        #     'tran_id': self.request.data['tran_id'],
        #     'val_id': self.request.data['val_id'],
        #     'amount': self.request.data['amount'],
        #     'card_type': self.request.data['card_type'],
        #     'store_amount': self.request.data['store_amount'],
        #     'card_no': self.request.data['card_no'],
        #     'bank_tran_id': self.request.data['bank_tran_id'],
        #     'status': self.request.data['status'],
        #     'tran_date': self.request.data['tran_date'],
        #     'currency': self.request.data['currency'],
        #     'card_issuer': self.request.data['card_issuer'],
        #     'card_brand': self.request.data['card_brand'],
        #     'card_issuer_country': self.request.data['card_issuer_country'],
        #     'card_issuer_country_code': self.request.data['card_issuer_country_code'],
        #     'store_id': self.request.data['store_id'],
        #     'verify_sign': self.request.data['verify_sign'],
        #     'verify_key': self.request.data['verify_key'],
        #     'currency_type': self.request.data['currency_type'],
        #     'currency_amount': self.request.data['currency_amount']
        # }
        # self.ssl_validation_res = self.SSLCommerz.validate_session(
        #     post_body)
