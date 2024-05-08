from django.db import models

from django.db.models.signals import pre_save
from django. utils. text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



def upload_location(instance, filename, **kwargs):
    file_path = 'scholarship-university-img/{filename}'.format(
        filename=filename
    )
    return file_path


def upload_location2(instance, filename, **kwargs):
    file_path = 'scholarship-icon-images/{filename}'.format(
        filename=filename
    )
    return file_path





def upload_location3(instance, filename, **kwargs):
    file_path = '{filename}'.format(
        filename=filename
    )
    return file_path



class Tag(models.Model):

    name                        = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
@receiver(post_save, sender=Tag)
def update_scholarship_tag_choices(sender, instance, created, **kwargs):
    if created:
        # Clear the choices cache to ensure updated tags appear in the dropdown
        Scholarship._meta.get_field('tags')._choices_cache = None



class Degree(models.Model):

    Degrees=(
        ('Phd', 'Phd'),
        ('Diploma', 'Diploma'),
        ('Masters', 'Masters'),
        ('Bachelor', 'Bachelor'),
    )

    name = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name





class Scholarship(models.Model):
    Fundings=(
        ('Fully funded', 'Fully funded'),
        ('Partially funded', 'Partially funded'),
        ('Underfunded', 'Underfunded'),
        ('Unfunded', 'Unfunded'),
        ('Self-funded', 'Self-funded'),
    )
    Tags=(
        ('icon1', 'icon1'),
        ('icon2', 'icon2'),
        ('icon3', 'icon3'),
        ('icon4', 'icon4'),
    )



    name                        = models.CharField(max_length=100, null=False, blank=False)
    University_name             = models.CharField(max_length=100, null=False, default="", blank=False)
    Scholarship_image           = models.ImageField(upload_to=upload_location2, null=True, blank=True)
    course                      = models.CharField(max_length=100, null=False, blank=True)
    eligibity                   = models.CharField(max_length=3000, null=False, blank=False)
    tags                        = models.ManyToManyField(Tag, related_name='scholarships')
    country                     = models.CharField(max_length=100, null=False, blank=False)
    completion_time             = models.DateField(null=False, default="0001-01-1",blank=True)
    closing_date                = models.DateField(null=False, blank=False)
    funding_status              = models.CharField(max_length=100, null=False, blank=False,choices=Fundings)
    degree                      = models.ManyToManyField(Degree, related_name='scholarships')
    course_Abbreviation         = models.CharField(max_length=100, default='', null=False, blank=True)
    subject                     = models.CharField(max_length=100, null=False,blank=True)
    sponsor                     = models.CharField(max_length=100,default='', null=False,blank=True)
    
    applicants                  = models.IntegerField( null=False,default=0, blank=False,)
    slug                        = models.SlugField(blank=True, max_length=200, unique=True)
    
    def save(self, *args, **kwargs):
        # deleting old image updating
        if self.pk:
            # Get the original instance from the database
            orig = type(self).objects.get(pk=self.pk)
            # If the image has changed, delete the old one
            if orig.Scholarship_image != self.Scholarship_image:
                orig.Scholarship_image.delete(save=False)

        super().save(*args, **kwargs)
        # saving before tagging to solve ID error
        tag_names = "- ".join(tag.name for tag in self.tags.all())
        closing_date_str = self.closing_date.strftime('%Y-%m-%d')
        self.slug = slugify(tag_names + "__" + closing_date_str + "__" + self.name)

        
        # Image cropping logic using Pillow
        if self.Scholarship_image:
            image_path = self.Scholarship_image.path
            img = Image.open(image_path)

            # Resize the image to fit within a 1200x370 box
            img.thumbnail((1200, 370))

            # Create a transparent background
            background = Image.new('RGBA', (1200, 370), (255, 255, 255, 255))

            # Calculate the position to paste the resized image (center)
            left = (1200 - img.width) // 2
            top = (370 - img.height) // 2

            # Paste the resized image onto the transparent background
            background.paste(img, (left, top))

            # Convert the image to RGB mode
            img_rgb = background.convert('RGB')

            # Save the processed image in PNG format
            output_io = BytesIO()
            img_rgb.save(output_io, format='PNG')
            output_io.seek(0)

                        # Delete the original image
            self.Scholarship_image.delete(save=False)

            # Save the processed image back to the original field
            file_path = upload_location3(self, self.Scholarship_image.name.split('/')[-1])
            self.Scholarship_image.save(file_path, ContentFile(output_io.getvalue()), save=False)
            
        


    def __str__(self):
        return self.name




class submitted_scholarship(models.Model):

    name                        = models.CharField(max_length=100, null=False, blank=False)
    user                        = models.CharField(max_length=100, null=False, blank=False)
    subject                     = models.CharField(max_length=100, null=False, blank=False)
    nationality                 = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    

    
class Universitie(models.Model):
    name                                  = models.CharField(max_length=100, null=False, blank=False)
    University_Scholarship_image          = models.ImageField(upload_to=upload_location, null=True, blank=False)

    def __str__(self):
        return self.name

    

    
class Guide(models.Model):

    name                        = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name





@receiver(post_delete, sender=Scholarship)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(save=False)



# Define a function to update the slug whenever the tags are modified
def update_slug_on_tags_changed(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        tag_names = "- ".join(tag.name for tag in instance.tags.all())
        closing_date_str = instance.closing_date.strftime('%Y-%m-%d')
        instance.slug = slugify(tag_names + "__" + closing_date_str + "__" + instance.name)
        instance.save()

# Connect the signal to the Scholarship model's m2m_changed signal
m2m_changed.connect(update_slug_on_tags_changed, sender=Scholarship.tags.through)
