from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import TestCRUD
from .serializers import ExpenceSerializer
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.views import APIView


class ExpenceListAPIView(ListCreateAPIView):
    serializer_class = ExpenceSerializer
    queryset = TestCRUD.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenceDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenceSerializer
    queryset = TestCRUD.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class SSLCommerzIPN(APIView):
    def post(self, request):
        post_prams = request.query_params
        return Response(post_prams)
