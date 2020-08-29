from django.shortcuts import render
from endpoint import Senator
from rest_framework import generics
from endpoint.serializers import ModelSerializer

# API Endpoint views
class listModels(generics.ListCreateAPIView):
    queryset = Senator.Model.objects.all()
    serializer_class = ModelSerializer

# Front-End Template Rendering
def homePage(request):
    senators = Senator.objects.all()

    data = {
        'first_name': first_name,
    }

    return render(request, 'endpoints/templates.html', data)
