from rest_framework import serializers

from scholarships.models import(
    Scholarship,
    Degree,
    Tag,
    submitted_scholarship,
    Guide,
    Universitie,
)

class ScholarshipSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()   
    # degree = serializers.SerializerMethodField()   

    class Meta:
        model = Scholarship
        fields = ['name', 'University_name', 'Scholarship_image', 'course', "eligibity", 'tags', 'country' , "completion_time","closing_date","funding_status",
                  "degree","course_Abbreviation","subject","sponsor","applicants","slug",
                  ]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
    # def get_degree(self, obj):
    #     return [degree.name for degree in obj.degree.all()]

class TagSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Tag
        # fields = ['name', 'price','Image']
        fields = ['name' ]


class Submitted_scholarshipSerializer(serializers.ModelSerializer):   

    class Meta:
        model = submitted_scholarship
        fields = ['name','user',"subject","nationality" ]

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

