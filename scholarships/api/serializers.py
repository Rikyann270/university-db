from rest_framework import serializers

from scholarships.models import(
    Scholarship,
    Tag,
    # Job,
    Guide,
    Universitie,
)

class ScholarshipSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Scholarship
        # fields = ['name', 'price','Image']
        fields = ['name', 'course', "eligibity", 'tags', 'country' , "completion_time","closing_date","funding_status",
                  "degree","course_Abbreviation","subject","sponsor","sponsor_Image","applicants",
                  ]


class TagSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Tag
        # fields = ['name', 'price','Image']
        fields = ['name' ]


# class JobSerializer(serializers.ModelSerializer):   

#     class Meta:
#         model = Job
#         fields = ['name' ]

class GuideSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Guide
        # fields = ['name', 'price','Image']
        fields = ['name' ]

class UniversitySerializer(serializers.ModelSerializer):   

    class Meta:
        model = Universitie
        # fields = ['name', 'price','Image']
        fields = ['name' ]

