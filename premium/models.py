from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Consultations (models.Model):
    course_consultations                = models.CharField(max_length=50, null=False, blank=False)
    course_consultations                = models.CharField(max_length=50, null=False, blank=False)
    professionals                       = models.CharField(max_length=50, null=False, blank=False)
  
    def __str__(self):
        return self.course_consultations
