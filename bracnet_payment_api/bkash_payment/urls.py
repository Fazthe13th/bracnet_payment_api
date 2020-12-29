from django.urls import path
from .views import BkashWebhookApiView
urlpatterns = [
    path('bkash_webhook/', BkashWebhookApiView.as_view(),
         name='bkash_webhook'),
]
