from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = 'scholarship_surponser_img/{filename}'.format(
        filename=filename
    )
    return file_path



class Scholarship(models.Model):
    Fundings=(
        ('option1', 'Fully funded'),
        ('option2', 'Partially funded'),
        ('option3', 'Underfunded'),
        ('option4', 'Unfunded'),
        ('option5', 'Self-funded'),
    )
    Degrees=(
        ('option1', 'Phd'),
        ('option2', 'Diploma'),
        ('option3', 'Masters'),
        ('option4', 'Bachelor'),
    )



    name                        = models.CharField(max_length=50, null=False, blank=False)
    course                      = models.CharField(max_length=50, null=False, blank=False)
    eligibity                   = models.CharField(max_length=50, null=False, blank=False)
    tag                         = models.CharField(max_length=50, null=False, blank=False)
    country                     = models.CharField(max_length=50, null=False, blank=False)
    completion_time             = models.DateField(null=False, blank=False)
    closing_date                = models.DateField(null=False, blank=False)
    funding_status              = models.CharField(max_length=50, null=False, blank=False,choices=Fundings)
    degree                      = models.CharField(max_length=50, null=False, blank=False,choices=Degrees)
    course_Abbreviation         = models.CharField(max_length=50, default='', null=False, blank=False)
    subject                     = models.CharField(max_length=50, null=False,blank=False)
    sponsor                     = models.CharField(max_length=50,default='', null=False,blank=False)
    sponsor_Image               = models.ImageField(upload_to=upload_location, null=True, blank=False)
    applicants                  = models.IntegerField( null=False, blank=False,)

    def __str__(self):
        return self.name




class University(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    
class Tag(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Job(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Guide(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name





def submission_delete(sender, instance, **kwargs):
    instance.sponsor_Image.delete(False)