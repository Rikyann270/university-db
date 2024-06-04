from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from collections import defaultdict


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
    country_Serializer,
    degree_Serializer,


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
        filters = self.request.query_params  # Get all filter parameters

        # Apply degree filter (using your existing logic)
        degree_filter = filters.get('degree')
        if degree_filter:
            queryset = queryset.filter(degree__icontains=degree_filter)

        # Add filtering logic for other parameters
        funding_status = filters.get('funding_status')
        if funding_status:
            queryset = queryset.filter(funding_status=funding_status)
            
        country = filters.get('country')
        if country:
            # queryset = queryset.filter(country=country)
            queryset = queryset.filter(country__icontains=country)

        subject = filters.get('subject')
        if subject:
            queryset = queryset.filter(subject__icontains=subject)

   

        return queryset
    


class ApicountryViewSet(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = country_Serializer

    def list(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Aggregate the data to numbers
        aggregated_data = defaultdict(lambda: {'country': None, 'land_mark': None, 'name': 0})

        for scholarship in queryset:
            country = scholarship.country
            land_mark = scholarship.land_mark.url if scholarship.land_mark else None
            
            if aggregated_data[country]['country'] is None:
                aggregated_data[country]['country'] = country
                aggregated_data[country]['land_mark'] = land_mark
            aggregated_data[country]['name'] += 1

        # Convert to list for data to be serailizer
        result = [{'country': data['country'], 'land_mark': data['land_mark'], 'scholarships': str(data['name'])} for data in aggregated_data.values()]
        print(len(result))
        return Response(result)

    

class ApidegreeViewSet(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = degree_Serializer

    def list(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Aggregate the data to numbers
        aggregated_data = defaultdict(lambda: {'degree': None, 'name': 0})

        for scholarship in queryset:
            degree = scholarship.degree
            
            if aggregated_data[degree]['degree'] is None:
                aggregated_data[degree]['degree'] = degree
            aggregated_data[degree]['name'] += 1

        # Convert to list for data to be serailizer
        result = [{'degree': data['degree'], 'scholarships': str(data['name'])} for data in aggregated_data.values()]
        print(len(result))
        return Response(result)

    




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


