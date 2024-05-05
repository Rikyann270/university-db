from rest_framework import serializers

from courses.models import(
    Course_detail,

)



class Course_detailSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Course_detail
        # fields = ['name', 'price','Image']
        fields = ['course_name','scholarship','universities_offering','jobs', 'cost',
                  'degree','course_Abbreviation','subject','Eligibility'
                  ]

