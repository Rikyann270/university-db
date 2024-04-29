from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = 'scholarship-surponser-img/{filename}'.format(
        filename=filename
    )
    return file_path


class Tag(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
@receiver(post_save, sender=Tag)
def update_scholarship_tag_choices(sender, instance, created, **kwargs):
    if created:
        # Clear the choices cache to ensure updated tags appear in the dropdown
        Scholarship._meta.get_field('tags')._choices_cache = None



class Scholarship(models.Model):
    Fundings=(
        ('Fully funded', 'Fully funded'),
        ('Partially funded', 'Partially funded'),
        ('Underfunded', 'Underfunded'),
        ('Unfunded', 'Unfunded'),
        ('Self-funded', 'Self-funded'),
    )
    Degrees=(
        ('Phd', 'Phd'),
        ('Diploma', 'Diploma'),
        ('Masters', 'Masters'),
        ('Bachelor', 'Bachelor'),
    )
    Tags=(
        ('icon1', 'icon1'),
        ('icon2', 'icon2'),
        ('icon3', 'icon3'),
        ('icon4', 'icon4'),
    )



    name                        = models.CharField(max_length=50, null=False, blank=False)
    University_name             = models.CharField(max_length=50, null=False, default="DEFAULT", blank=False)
    course                      = models.CharField(max_length=50, null=False, blank=False)
    eligibity                   = models.CharField(max_length=3000, null=False, blank=False)
    # tag                         = models.CharField(max_length=50, null=False, blank=False,choices=Tags)
    tags                        = models.ManyToManyField(Tag, related_name='scholarships')
    country                     = models.CharField(max_length=50, null=False, blank=False)
    completion_time             = models.DateField(null=False, blank=False)
    closing_date                = models.DateField(null=False, blank=False)
    funding_status              = models.CharField(max_length=50, null=False, blank=False,choices=Fundings)
    degree                      = models.CharField(max_length=50, null=False, blank=False,choices=Degrees)
    course_Abbreviation         = models.CharField(max_length=100, default='', null=False, blank=False)
    subject                     = models.CharField(max_length=100, null=False,blank=False)
    sponsor                     = models.CharField(max_length=50,default='', null=False,blank=False)
    sponsor_Image               = models.ImageField(upload_to=upload_location, null=True, blank=False)
    applicants                  = models.IntegerField( null=False, blank=False,)
    slug                        = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name




class submitted_scholarship(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)
    user                        = models.CharField(max_length=50, null=False, blank=False)
    subject                     = models.CharField(max_length=100, null=False, blank=False)
    nationality                 = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Universitie(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Universitie(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    

    
class Guide(models.Model):

    name                        = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name





@receiver(post_delete, sender=Scholarship)
def submission_delete(sender, instance, **kwargs):
    instance.sponsor_Image.delete(save=False)


def pre_save_scholarship_receiver(sender, instance, *args, **kwargs):


    if not instance.slug:
        instance.slug = slugify(instance.tags + "-" + instance.name)

       

pre_save.connect(pre_save_scholarship_receiver, sender=Scholarship)
