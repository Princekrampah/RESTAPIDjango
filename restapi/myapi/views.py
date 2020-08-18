from django.shortcuts import render
from .models import Employee, Occupation
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.


class EmployeeListCreatView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

