from django.shortcuts import render

# Create your views here.

# added Unnat
from rest_framework import generics, permissions,status, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import ClientSerializer, RegisterSerializer

from .models import Client
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": ClientSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# for :: model viewset :: automatic basic CRUD functionalities
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer    

# for :: model viewset

# from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.response import Response

# from student import serializers
# from student import models


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer