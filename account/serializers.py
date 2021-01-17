from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Person
		fields 	= '__all__'

class RelativeSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Relative
		fields 	= ['first_name', 'last_name', 'patronymic']

class IndividualSerializer(serializers.ModelSerializer):
	relatives = RelativeSerializer(many = True)
	class Meta:
		model 	= Individual
		fields 	= ['first_name', 'last_name', 'patronymic', 'relatives']


	def create(self, validated_data):
		relatives_data 	= validated_data.pop('relatives')
		individual 		= Individual.objects.create(**validated_data)
		for relative_data in relatives_data:
			Relative.objects.create(individual = individual, **relative_data)
		return individual
