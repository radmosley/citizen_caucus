from django.shortcuts import render
from endpoint import models
from rest_framework import generics
from endpoint.serializers import ModelSerializer

# API Endpoint views
class listModels(generics.ListCreateAPIView):
    queryset = models.Model.objects.all()
    serializer_class = ModelSerializer
