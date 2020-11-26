from django.urls import path
from .views import SslcommerzPaymentInitializationView

urlpatterns = [
    path('initialize/', SslcommerzPaymentInitializationView.as_view(),
         name='sslc_initialize'),
    # path('<int:id>', ExpenceDetailAPIView.as_view(), name='expense'),
    # path('test_post_parms', SSLCommerzIPN.as_view(), name='SSLCommerzIPN')
]
