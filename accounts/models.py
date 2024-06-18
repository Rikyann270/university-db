from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from courses.models import Subject


class MyAccountManager(BaseUserManager):
    def create_user(self, username,first_name, second_name, email,phone_number,date_of_birth,citizenship,
                    zip_code,school_level,high_school_name,graduation_date,presently_attending_college,
                    colleges_of_interest,degree_of_pursuit,field_of_study,overall_GPA,career_goal,gender,ethnic_background,
                    password=None
                    ):
        # if not first_name:
        #     raise ValueError("Please check the username")
        
        # if not phone_number:
        #     raise ValueError("Please check the phone number")
        

        user = self.model(
            username                    =   username,
            first_name                  =   first_name,                 
            second_name                 =   second_name,                
            email                       =   self.normalize_email(email),
            phone_number                =   phone_number,               
            date_of_birth               =   date_of_birth,              
            citizenship                 =   citizenship,                
            zip_code                    =   zip_code,                   
            school_level                =   school_level,               
            high_school_name            =   high_school_name,           
            graduation_date             =   graduation_date,            
            presently_attending_college =   presently_attending_college,
            colleges_of_interest        =   colleges_of_interest,       
            degree_of_pursuit           =   degree_of_pursuit,          
            field_of_study              =   field_of_study,             
            overall_GPA                 =   overall_GPA,                
            career_goal                 =   career_goal,                
            gender                      =   gender,                     
            ethnic_background           =   ethnic_background,          
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, first_name, second_name, email,phone_number,
                         date_of_birth,citizenship,
                    zip_code,school_level,high_school_name,graduation_date,presently_attending_college,
                    colleges_of_interest,degree_of_pursuit,field_of_study,overall_GPA,career_goal,gender,ethnic_background,
                    password=None):
        user = self.create_user(
                username                    =   username,
                first_name                  =   first_name,                 
                second_name                 =   second_name,                
                email                       =   self.normalize_email(email),
                phone_number                =   phone_number,               
                date_of_birth               =   date_of_birth,              
                citizenship                 =   citizenship,                
                zip_code                    =   zip_code,                   
                school_level                =   school_level,               
                high_school_name            =   high_school_name,           
                graduation_date             =   graduation_date,            
                presently_attending_college =   presently_attending_college,
                colleges_of_interest        =   colleges_of_interest,       
                degree_of_pursuit           =   degree_of_pursuit,          
                field_of_study              =   field_of_study,             
                overall_GPA                 =   overall_GPA,                
                career_goal                 =   career_goal,                
                gender                      =   gender,                     
                ethnic_background           =   ethnic_background,
                password                    =   password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    # Degree_pursuit=(
    #     ('Phd', 'Phd'),
    #     ('Diploma', 'Diploma'),
    #     ('Masters', 'Masters'),
    #     ('Bachelor', 'Bachelor'),
    #     ('Research', 'Research'),

    #         )
    # gender_fl=(
    #     ('male', 'male'),
    #     ('female', 'female'),
    #     ('other', 'other'),


    #         )
    # gpa_fl=(
    #     ('N/A', 'N/A'),
    #     ('2.0', '2.0'),
    #     ('2.1', '2.1'),
    #     ('2.2', '2.2'),
    #     ('2.3', '2.3'),
    #     ('2.4', '2.4'),
    #     ('2.5', '2.5'),
    #     ('2.6', '2.6'),
    #     ('2.7', '2.7'),
    #     ('2.8', '2.8'),
    #     ('2.9', '2.9'),
    #     ('3.0', '3.0'),
    #     ('3.1', '3.1'),
    #     ('3.2', '3.2'),
    #     ('3.3', '3.3'),
    #     ('3.4', '3.4'),
    #     ('3.5', '3.5'),
    #     ('3.6', '3.6'),
    #     ('3.7', '3.7'),
    #     ('3.8', '3.8'),
    #     ('3.9', '3.9'),
    #     ('4.0', '4.0'),
    #         )
    # career_goal_fl=(
    #     ('Art,Design or Fasion', 'Art,Design or Fasion'),
    #     ('Beauty or Cosmetology', 'Beauty or Cosmetology'),
    #     ('Marketing, Business or Management', 'Marketing, Business or Management'),
    #     ('Computers, IT or Techinology', 'Computers, IT or Techinology'),
    #     ('Culinary Arts', 'Culinary Arts'),
    #     ('Health Care ,Nursing', 'Health Care ,Nursing'),
    #     ('Law,Criminal Justice', 'Law,Criminal Justice'),
    #     ('Teaching / Education', 'Teaching / Education'),




    #         )
    
    first_name 					= models.CharField(max_length=30, blank=True, null=True )
    second_name 				= models.CharField(max_length=30, blank=True, null=True )
    username                    = models.CharField(max_length=100, blank=True, null=True, unique=True )
    email 					    = models.EmailField(verbose_name="email", blank=True, max_length=100, unique=True)
    phone_number                = models.CharField(max_length=13, blank=True, null=True )
    date_of_birth 		    	= models.DateField(null=True,blank=True)
    citizenship                 = models.CharField(max_length=40, blank=True, null=True )
    zip_code                    = models.CharField(max_length=40, blank=True, null=True )
    school_level                = models.CharField(max_length=40, blank=True, null=True )
    high_school_name            = models.CharField(max_length=100, blank=True, null=True )
    graduation_date             = models.DateField(null=True,blank=True)
    presently_attending_college =models.BooleanField(default=True)
    colleges_of_interest        =models.CharField(max_length=100, blank=True, null=True )
    degree_of_pursuit           =models.CharField(max_length=40, blank=True, null=True )
    field_of_study              =models.CharField(max_length=40, blank=True, null=True )
    overall_GPA                 =models.CharField(max_length=40, blank=True, null=True )
    career_goal                 =models.CharField(max_length=40, blank=True, null=True )
    gender                      =models.CharField(max_length=40, blank=True, null=True )
    ethnic_background           =models.CharField(max_length=40, blank=True, null=True )
    
    
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=True)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=True)
    is_superuser			= models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email','first_name','second_name','phone_number','date_of_birth',
                       'citizenship','zip_code','school_level','high_school_name','graduation_date',
                       'presently_attending_college','colleges_of_interest','degree_of_pursuit','field_of_study',
                       'overall_GPA','career_goal','gender','ethnic_background',]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=True, **kwargs):
    if created:
        Token.objects.create(user=instance)