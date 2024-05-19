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
from django.core.validators import URLValidator



def upload_location(instance, filename, **kwargs):
    file_path = 'university-img/{filename}'.format(
        filename=filename
    )
    return file_path


def upload_location3(instance, filename, **kwargs):
    file_path = '{filename}'.format(
        filename=filename
    )
    return file_path


def upload_location2(instance, filename, **kwargs):
    file_path = 'scholarship-icon-images/{filename}'.format(
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
    default_image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxKE79UQ0gtUhWuaqAs_NILmAYcOPAnItgwo2BPMOLsw&s" 


    name                        = models.CharField(max_length=100, null=False, blank=False)
    University_name             = models.CharField(max_length=100, null=False, blank=False)
    Scholarship_image           = models.ImageField(upload_to=upload_location2, null=True, blank=True, max_length=500,)
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
            img = Image.open(image_path).convert('RGB')


            # Resize the image to fit within a 1200x370 box
            
            img.thumbnail((1200, 370))
            print(img.thumbnail,"this is image size")
            

            # Create a transparent background
            background = Image.new('RGBA', (700, img.height), (255, 250, 250, 255))
            

            # Calculate the position to paste the resized image (center)
            left = (700 - img.width) // 2
            top = (img.height - img.height) //2

            # Delete the original gfdgvbfdvb
            default_storage.delete(image_path)

            # Paste the resized image onto the transparent background 
            background.paste(img, (left,top))

            # Convert the image to RGB mode some errors fixed
            img_rgb = background.convert('RGB')


            # Save the processed image in PNG format
            output_io = BytesIO()
            img_rgb.save(output_io, format='PNG')
            output_io.seek(0)

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
    





# class Link(models.Model):
#     url = models.URLField(validators=[URLValidator])
#     description = models.CharField(max_length=255, blank=True)  # Optional

class Universitie(models.Model):
    name                                  = models.CharField(max_length=150, null=False, blank=False)
    University_image                      = models.ImageField(upload_to=upload_location, null=True, blank=True, max_length=500,)
    
    domain1                               = models.CharField(max_length=100, null=True, blank=True)
    domain2                               = models.CharField(max_length=100, null=True, blank=True)
    domain3                               = models.CharField(max_length=100, null=True, blank=True)
    domain4                               = models.CharField(max_length=100, null=True, blank=True)
    webpage1                              = models.CharField(max_length=100, null=True, blank=True)
    webpage2                              = models.CharField(max_length=100, null=True, blank=True)
    webpage3                              = models.CharField(max_length=100, null=True, blank=True)
    webpage4                              = models.CharField(max_length=100, null=True, blank=True)
    country                               = models.CharField(max_length=100, null=True, blank=True)
    alpha_two_code                        = models.CharField(max_length=5   , null=True, blank=True)
    state_province                        = models.CharField(max_length=100, null=True, blank=True)
   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Check if University_image is already set or not
        if not self.University_image:
            # Iterate through web page URLs to find the logo
            for i in range(1, 5):
                webpage_field = f'webpage{i}'
                logo_url = getattr(self, webpage_field)
                if logo_url:
                    try:
                        # Fetch the image from the URL
                        response = requests.get(logo_url)
                        if response.status_code == 200:
                            # Save the image to University_image field
                            self.University_image.save(f'university_logo_{self.pk}.png', File(BytesIO(response.content)))
                            break  # Exit loop if image successfully saved
                    except Exception as e:
                        print(f"Error downloading logo for {self.name}: {e}")

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
