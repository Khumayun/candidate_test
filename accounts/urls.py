from django.urls import path
from .views import *
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
    path('createUser/', CreateUser.as_view()),
    path('createIndividual/', ListCreateAPIView.as_view(queryset = Individual.objects.all(), serializer_class = IndividualSerializer)),
    path('createRelative/', ListCreateAPIView.as_view(queryset = Relative.objects.all(), serializer_class = RelativeSerializer)),
    path('api-token-auth/', CustomAuthToken.as_view()),
]
