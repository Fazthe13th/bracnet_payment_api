from django.urls import path
from .views import ExpenceDetailAPIView, ExpenceListAPIView, SSLCommerzIPN

urlpatterns = [
    path('', ExpenceListAPIView.as_view(), name='expense'),
    path('<int:id>', ExpenceDetailAPIView.as_view(), name='expense'),
    path('test_post_parms', SSLCommerzIPN.as_view(), name='SSLCommerzIPN')
]
