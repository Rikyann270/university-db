from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 

from courses.models import(
    Course_detail,

)

from courses.api.serializers import (
    Course_detailSerializer,

    )



@api_view(['GET', ])
def api_course_detail_view(request, slug):
    try:
        Course_detail_info=Course_detail.objects.get(slug=slug)
    except Course_detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = Course_detailSerializer(Course_detail_info)
        return Response(serializer.data)
    




class ApiscourseSerializerListView(ListAPIView):
    queryset = Course_detail.objects.all()
    serializer_class = Course_detailSerializer
    pagination_class = PageNumberPagination
    # searching


