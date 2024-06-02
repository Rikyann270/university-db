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
        # fields = ["degree",
        #           ]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
    # def get_degree(self, obj):
    #     return [degree.name for degree in obj.degree.all()]



class University_country_Serializer(serializers.ModelSerializer):
    Scholarship = serializers.CharField(source='name')
    country2 = serializers.SerializerMethodField()

    class Meta:
        model = Scholarship
        fields = ['Scholarship', 'University_name',  'country','country2'
        ]
        

    # def get_country2(self, obj):
    #     universities = Universitie.objects.filter(country=obj.country)
    #     if universities.exists():
    #         # Return the country of the first matching University or handle multiple results as needed
    #         print(universities,"thisssss")

    #         return universities.first().country
    #     return None

    def get_country2(self, obj):
        # check if scholar match univ
        universities = Universitie.objects.filter(name=obj.University_name)
        if universities.exists():
            # Concatenate the countries of all matching universities
            countries = ', '.join(university.name for university in universities if university.name)

            return countries
        return None




class TagSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Tag
        
        fields = ['name' ]


class Submitted_scholarshipSerializer(serializers.ModelSerializer):   

    class Meta:
        model = submitted_scholarship
        fields = ['name','user',"subject","nationality" ]

class GuideSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Guide
        
        fields = ['name' ]

class UniversitySerializer(serializers.ModelSerializer):   

    class Meta:
        model = Universitie
        
        fields = ['name' ]

