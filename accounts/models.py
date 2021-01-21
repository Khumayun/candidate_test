from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class Person(AbstractUser):
	patronymic	= models.CharField(max_length = 120)

	def get_full_name(self):
		full_name = '%s %s %s' % (self.last_name, self.first_name, self.patronymic)
		return full_name.strip()

	def get_short_name(self):
		short_name = '%s %s' % (self.last_name, self.first_name)
		return short_name.strip()

class Individual(models.Model):
	first_name	= models.CharField(max_length = 120)
	last_name	= models.CharField(max_length = 120)
	patronymic	= models.CharField(max_length = 120)

class Relative(models.Model):
	individual	= models.ForeignKey(Individual, on_delete=models.CASCADE, related_name = 'relatives')
	first_name	= models.CharField(max_length = 120)
	last_name	= models.CharField(max_length = 120)
	patronymic	= models.CharField(max_length = 120)
	kinship 	= models.CharField(max_length = 120)

	def __str__(self):
		return '%d: %s' % (self.order, self.first_name)

@receiver(post_save, sender=Person)
def create_token(sender, instance, created, **kwargs):
	if created:
		Token.objects.create(user = instance)		#if new user was created attach a token to it