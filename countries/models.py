from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import m2m_changed




def upload_location4(instance, filename, **kwargs):
    file_path = 'land_mark-img/{filename}'.format(
        filename=filename
    )
    return file_path


class Country_details(models.Model):

    country_name                    = models.CharField(max_length=50, null=False, blank=False)
    phone_code                      = models.CharField(max_length=10, null=False, blank=False)
    country_code                    = models.CharField(max_length=10, null=False, blank=False)
    land_mark                       = models.ImageField(upload_to=upload_location4, null=False, blank=True, max_length=500,)
    land_mark_url                   = models.CharField(max_length=300, null=False, blank=True)
 
    

    def __str__(self):
        return self.country_name
    
@receiver(post_delete, sender=Country_details)
def submission_delete(sender, instance, **kwargs):
    if instance.land_mark:
        instance.land_mark.delete(save=False)

