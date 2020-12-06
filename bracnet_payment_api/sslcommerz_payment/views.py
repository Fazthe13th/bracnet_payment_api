from .models import SslcommerzPaymentInitializationModel, SslcommerzPaymentValidateModel
from .serializers import SslcommerzPaymentInitializationSerializer, SslcommerzIPNSerializer, SslcommerzValidationSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from django.db import DatabaseError, DataError
from django.shortcuts import redirect
from rest_framework.reverse import reverse
from . SslcommerzAPICall.sslcommerz import SSLCommerzfunc
import uuid
import os
import json


class SslcommerzPaymentInitializationView(ListCreateAPIView):
    serializer_class = SslcommerzPaymentInitializationSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = SslcommerzPaymentInitializationModel.objects.all()
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sslc_tran_uuid = uuid.uuid4()
        try:
            post_body = {
                'tran_id': sslc_tran_uuid,
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
                serializer.save(tran_id=sslc_tran_uuid,
                                status=self.sslc_response['status'], failed_reason=self.sslc_response['failedreason'])
                return Response({'error': 'SSLCommerz session creation failed',
                                 'failed_reason': self.sslc_response['failedreason']}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer.save(tran_id=sslc_tran_uuid,
                            status=self.sslc_response['status'], failed_reason=self.sslc_response['failedreason'])
            return Response({'msg': 'SSLCommerz session created',
                             'payment_url': self.sslc_response['GatewayPageURL']}, status=status.HTTP_200_OK)
        except DatabaseError:
            return Response({'error': 'Database error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SslcommerzPaymentInitializationRetrive(RetrieveAPIView):
    serializer_class = SslcommerzPaymentInitializationSerializer
    queryset = SslcommerzPaymentInitializationModel.objects.all()
    # permission_classes = (permissions.IsAuthenticated)
    lookup_field = 'tran_id'

    # def get_queryset(self):
    #     print("This is the request" + str(self.request.GET))
    #     return self.queryset.filter(tran_id=self.request.tran_id)


class SSLCommerzIPNView(GenericAPIView):
    serializer_class = SslcommerzIPNSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    SSLCommerz = SSLCommerzfunc()

    def post(self, request):
        try:
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if request.data.get('val_id') is not None:
                print('In the val_id condition')
                self.ssl_validation_res = self.SSLCommerz.validate_session(
                    request.data['val_id'])
            else:
                print('val_id is none')
                self.ssl_validation_res = {
                    'status': request.data['status'],
                    'tran_date': request.data['tran_date'],
                    'tran_id': request.data['tran_id'],
                    'val_id': None,
                    'amount': request.data['amount'],
                    'store_amount': 0.00,
                    'currency': request.data['currency'],
                    'bank_tran_id': request.data['bank_tran_id'],
                    'card_type': request.data['card_type'],
                    'card_no': request.data['card_no'],
                    'card_issuer': request.data['card_issuer'],
                    'card_brand': request.data['card_brand'],
                    'card_issuer_country': request.data['card_issuer_country'],
                    'card_issuer_country_code': request.data['card_issuer_country_code'],
                    'currency_type': request.data['currency_type'],
                    'currency_amount': request.data['currency_amount'],
                    'currency_rate': request.data['currency_rate'],
                    'base_fair': request.data['base_fair'],
                    'value_a': request.data['value_a'],
                    'value_b': request.data['value_b'],
                    'value_c': request.data['value_c'],
                    'value_d': request.data['value_d'],
                    'emi_instalment': '0',
                    'emi_amount': '0.00',
                    'emi_description': None,
                    'emi_issuer': None,
                    'account_details': None,
                    'risk_title': 'N/A',
                    'risk_level': 'N/A',
                    'APIConnect': None,
                    'validated_on': None,
                    'gw_version': '',
                    'offer_avail': 0,
                    'card_ref_id': 'N/A',
                    'discount_percentage': '0',
                    'discount_amount': '0',
                    'discount_remarks': None,
                    'isTokeizeSuccess': 0,
                    'campaign_code': ''
                }
            print(self.ssl_validation_res)
            validation_table_serializer = SslcommerzValidationSerializer(
                data=self.ssl_validation_res)
            validation_table_serializer.is_valid(raise_exception=True)
            validation_table_serializer.save()
            return Response({'msg': 'Payment IPN received and Validated'}, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'msg': 'SSLCommarz validation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SSLCommerzValidatedList(ListAPIView):
    serializer_class = SslcommerzValidationSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = SslcommerzPaymentValidateModel.objects.all()


class SSLCommerzValidatedRetrive(RetrieveAPIView):
    serializer_class = SslcommerzValidationSerializer
    queryset = SslcommerzPaymentValidateModel.objects.all()
    # permission_classes = (permissions.IsAuthenticated)
    lookup_field = 'tran_id'

    # def get_queryset(self):
    #     return self.queryset.filter(tran_id=self.request.tran_id)
