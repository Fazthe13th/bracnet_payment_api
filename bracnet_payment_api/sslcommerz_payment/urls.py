from django.urls import path
from .views import SslcommerzPaymentInitializationView, SSLCommerzIPNView, SSLCommerzValidateView

urlpatterns = [
    path('initialize/', SslcommerzPaymentInitializationView.as_view(),
         name='sslc_initialize'),
    path('sslc_ipn/', SSLCommerzIPNView.as_view(), name='sslc_ipn'),
    path('sslc_payment_validate/<validation_data>/', SSLCommerzValidateView.as_view(),
         name='sslc_payment_validate'),
    # path('<int:id>', ExpenceDetailAPIView.as_view(), name='expense'),
    # path('test_post_parms', SSLCommerzIPN.as_view(), name='SSLCommerzIPN')
]
