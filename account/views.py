from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *

class CreateUser(ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class createIndividual(ListCreateAPIView):
	queryset = Individual.objects.all()
	serializer_class = IndividualSerializer

class createRelative(ListCreateAPIView):
	queryset = Relative.objects.all()
	serializer_class = RelativeSerializer