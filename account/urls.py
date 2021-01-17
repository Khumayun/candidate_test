from django.urls import path
from .views import *

urlpatterns = [
    path('createUser/', CreateUser.as_view()),
    path('createIndividual/', createIndividual.as_view()),
    path('createRelative/', createRelative.as_view()),
]
