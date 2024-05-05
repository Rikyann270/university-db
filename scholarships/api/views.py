from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 

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





class ApischolarshipsListView(ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    pagination_class = PageNumberPagination
        #searching
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'University_name', 'course')


class Apisubmitted_scholarshipListView(ListAPIView):
    queryset = submitted_scholarship.objects.all()
    serializer_class = Submitted_scholarshipSerializer
    pagination_class = PageNumberPagination


