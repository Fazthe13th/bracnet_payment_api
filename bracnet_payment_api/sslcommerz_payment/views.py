from .models import SslcommerzPaymentInitialization
from .serializers import SslcommerzPaymentInitializationSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from django.db import DatabaseError, DataError
from django.shortcuts import redirect
from . SslcommerzAPICall.initialize_payment import SSLCommerzInitialize
import uuid
import os


class SslcommerzPaymentInitializationView(ListCreateAPIView):
    serializer_class = SslcommerzPaymentInitializationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SslcommerzPaymentInitialization.objects.all()
    sslc_tran_uuid = uuid.uuid4()
    SSLCommerz = SSLCommerzInitialize()

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
