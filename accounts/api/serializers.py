from rest_framework import serializers
from accounts.models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'username','first_name','second_name','phone_number','date_of_birth',
                    'citizenship','zip_code','school_level','high_school_name','graduation_date',
                    'presently_attending_college','colleges_of_interest','degree_of_pursuit','field_of_study',
                    'overall_GPA','career_goal','gender','ethnic_background','password',
                    ]
        extra_kwargs = { 
                    'password': {'write_only' : True}
        }

    def save(self):
        accounts = Account(
                    first_name                  =self.validated_data['first_name'],
                    second_name                 =self.validated_data['second_name'],
                    email                       =self.validated_data['email'],
                    username                       =self.validated_data['username'],
                    phone_number                =self.validated_data['phone_number'],
                    date_of_birth               =self.validated_data['date_of_birth'],
                    citizenship                 =self.validated_data['citizenship'],
                    zip_code                    =self.validated_data['zip_code'],
                    school_level                =self.validated_data['school_level'],
                    high_school_name            =self.validated_data['high_school_name'],
                    graduation_date             =self.validated_data['graduation_date'],
                    presently_attending_college =self.validated_data['presently_attending_college'],
                    colleges_of_interest        =self.validated_data['colleges_of_interest'],
                    degree_of_pursuit           =self.validated_data['degree_of_pursuit'],
                    field_of_study              =self.validated_data['field_of_study'],
                    overall_GPA                 =self.validated_data['overall_GPA'],
                    career_goal                 =self.validated_data['career_goal'],
                    gender                      =self.validated_data['gender'],
                    ethnic_background           =self.validated_data['ethnic_background'],
                    

        )
        password = self.validated_data['password']

        accounts.set_password(password)
        accounts.save()
        return accounts
    

class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name','second_name','phone_number','date_of_birth',
            'citizenship','zip_code','school_level','high_school_name','graduation_date',
            'presently_attending_college','colleges_of_interest','degree_of_pursuit','field_of_study',
            'overall_GPA','career_goal','gender','ethnic_background',
            ]

class AccountPropertiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username','first_name','second_name','phone_number','date_of_birth',
                    'citizenship','zip_code','school_level','high_school_name','graduation_date',
                    'presently_attending_college','colleges_of_interest','degree_of_pursuit','field_of_study',
                    'overall_GPA','career_goal','gender','ethnic_background','password'
                    ]