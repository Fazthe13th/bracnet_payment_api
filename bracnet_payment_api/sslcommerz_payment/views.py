from .models import SslcommerzPaymentInitializationModel, SslcommerzPaymentValidateModel
from .serializers import SslcommerzPaymentInitializationSerializer, SslcommerzIPNSerializer, SslcommerzValidationSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.db import DatabaseError, DataError
from django.shortcuts import redirect
from rest_framework.reverse import reverse
from django.http import HttpResponsePermanentRedirect
from . SslcommerzAPICall.sslcommerz import SSLCommerzfunc
import uuid
import os
import json


# Custom redect to redict to HTTP sites


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['http', 'https']


class SslcommerzPaymentInitializationView(ListCreateAPIView):
    serializer_class = SslcommerzPaymentInitializationSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = SslcommerzPaymentInitializationModel.objects.all()
    sslc_tran_uuid = uuid.uuid4()
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
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
    # permission_classes = (permissions.IsAuthenticated,)
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.ssl_validation_res = self.SSLCommerz.validate_session(
            request.data['val_id'])
        validation_table_serializer = SslcommerzValidationSerializer(
            data=self.ssl_validation_res)
        validation_table_serializer.is_valid(raise_exception=True)
        validation_table_serializer.save()
        return Response({'msg': 'Validated'})
        try:
            pass
        except Exception:
            return Response({'msg': 'SSLCommarz validation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SSLCommerzValidateView(GenericAPIView):
    serializer_class = SslcommerzValidationSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    SSLCommerz = SSLCommerzfunc()
    queryset = SslcommerzPaymentValidateModel.objects.all()

    def get(self, request, validation_data):
        converted_validation_data = json.loads(validation_data)
        serializer = self.serializer_class(data=converted_validation_data)
        serializer.is_valid(raise_exception=True)
        print(converted_validation_data)
        try:
            self.ssl_validation_res = self.SSLCommerz.validate_session(
                converted_validation_data['val_id'])
            print(self.ssl_validation_res)
            # try:
            #     serializer.save()
            # except DatabaseError:
            #     raise DatabaseError(
            #         'Database crud has failed. Contact developer.')
            return Response({'msg': 'Validated'})
        except Exception:
            raise Exception('Validation with SSLCommerz validation api failed')
