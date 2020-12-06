from django.urls import path
from .views import SslcommerzPaymentInitializationView, SslcommerzPaymentInitializationRetrive, SSLCommerzIPNView, SSLCommerzValidatedList, SSLCommerzValidatedRetrive

urlpatterns = [
    path('initialize/', SslcommerzPaymentInitializationView.as_view(),
         name='sslc_initialize'),
    path('sslc_payment_initizlize_retrive_by_train_id/<tran_id>/', SslcommerzPaymentInitializationRetrive.as_view(),
         name='sslc_payment_initizlize_retrive_by_train_id'),
    path('sslc_ipn/', SSLCommerzIPNView.as_view(), name='sslc_ipn'),
    path('sslc_payment_validate_list/', SSLCommerzValidatedList.as_view(),
         name='sslc_payment_validate_list'),
    path('sslc_payment_validate_retrive_by_train_id/<tran_id>/', SSLCommerzValidatedRetrive.as_view(),
         name='sslc_payment_validate_retrive_by_train_id'),
    # path('<int:id>', ExpenceDetailAPIView.as_view(), name='expense'),
    # path('test_post_parms', SSLCommerzIPN.as_view(), name='SSLCommerzIPN')
]
