from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


from scholarships.models import(
    Scholarship,
    Tag,
    # Job,
    Guide,
    Universitie,
    submitted_scholarship,
    
)

from scholarships.api.serializers import (
    ScholarshipSerializer,
    TagSerializer,
    # JobSerializer,
    GuideSerializer,
    UniversitySerializer,
    Submitted_scholarshipSerializer,
    University_country_Serializer,


    )



@api_view(['GET', ])
def api_scholarship_detail_view(request, slug):
    try:
        scholarship_info=Scholarship.objects.get(slug=slug)
    except Scholarship.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = ScholarshipSerializer(scholarship_info)
        return Response(serializer.data)
    




class ApistagSerializerListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination


# class ApijobSerializerListView(ListAPIView):
#     queryset = Scholarship.objects.all()
#     serializer_class = JobSerializer
#     pagination_class = PageNumberPagination


class ApiguideSerializerListView(ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    pagination_class = PageNumberPagination


class ApiuniversitySerializerListView(ListAPIView):
    queryset = Universitie.objects.all()
    serializer_class = UniversitySerializer
    pagination_class = PageNumberPagination

# University_country_Serializer
class Api_University_country_SerializerListView(ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = University_country_Serializer
    pagination_class = PageNumberPagination


# api filter    
class ApischolarshipViewSet(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'University_name', 'course', "eligibity", 'tags', 'country' , "completion_time","closing_date","funding_status",
                  "degree","course_Abbreviation","subject","applicants","slug",
                  ]
    def filter_queryset(self, queryset):
        
        # Apply the custom degree filter
        degree_filter = self.request.query_params.get('degree')
        if degree_filter:
            queryset = queryset.filter(degree__icontains=degree_filter)

        else:
             queryset = super().filter_queryset(queryset)


        
        return queryset
    




class ApischolarshipsListView(ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    pagination_class = PageNumberPagination
        #searching
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'University_name', 'course','degree')

    




class Apisubmitted_scholarshipListView(ListAPIView):
    queryset = submitted_scholarship.objects.all()
    serializer_class = Submitted_scholarshipSerializer
    pagination_class = PageNumberPagination


