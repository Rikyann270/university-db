from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import m2m_changed




def upload_location1(instance, filename, **kwargs):
    file_path = 'main-images/{filename}'.format(
        filename=filename
    )
    return file_path

def upload_location2(instance, filename, **kwargs):
    file_path = 'featured-image/{filename}'.format(
        filename=filename
    )
    return file_path


class Main_image(models.Model):

    main_image                   = models.ImageField(upload_to=upload_location1, null=True, blank=True, max_length=200,)
 
    

    def __str__(self):
        return self.main_image.url if self.main_image else "No Image"
    

class Featured_image(models.Model):

    featured_image                   = models.ImageField(upload_to=upload_location2, null=True, blank=True, max_length=200,)
 
    

    def __str__(self):
        return self.featured_image.url if self.featured_image else "No Image"
    







@receiver(post_delete, sender=Main_image)
def submission_delete(sender, instance, **kwargs):
    if instance.main_image:
        instance.main_image.delete(save=False)

@receiver(post_delete, sender=Featured_image)
def submission_delete(sender, instance, **kwargs):
    if instance.featured_image:
        instance.featured_image.delete(save=False)

