from django.http import QueryDict
from django.shortcuts import render
from rest_framework import  viewsets
from numbers_api.models import Number
from numbers_api.serializer import NumberSerializer

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    http_method_names = ['get']