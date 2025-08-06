from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializers
from .models import MovieData

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = Movieserializers


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ = 'action')
    serializer_class = Movieserializers

class AdvantureViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ = 'advanture')
    serializer_class = Movieserializers
