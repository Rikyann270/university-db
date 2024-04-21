from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


# def upload_location(instance, filename, **kwargs):
#     file_path = 'scholarship_surponser_img/{filename}'.format(
#         filename=filename
#     )
#     return file_path

class Course_detail(models.Model):
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



    name                             = models.CharField(max_length=50, null=False, blank=False)
    course_name                      = models.CharField(max_length=50, null=False, blank=False)
    scholarship                      = models.CharField(max_length=50, null=False, blank=False)
    universities_offering            = models.CharField(max_length=50, null=False, blank=False)
    jobs                             = models.CharField(max_length=50, null=False, blank=False)
    cost                             = models.CharField(max_length=50, null=False, blank=False,choices=Fundings)
    degree                           = models.CharField(max_length=50, null=False, blank=False,choices=Degrees)
    course_Abbreviation              = models.CharField(max_length=50, default='', null=False, blank=False)
    subject                          = models.CharField(max_length=50, null=False,blank=False)
    Eligibility                      = models.CharField(max_length=50,default='', null=False,blank=False)

    def __str__(self):
        return self.name
