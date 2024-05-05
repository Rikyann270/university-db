from django.urls import path

from courses.api.views import (
    # single
    api_course_detail_view,
    #list
    ApiscourseSerializerListView,


    )

app_name = 'courses'

urlpatterns = [
    # path('<slug>/', api_course_detail_view, name="detail"),
    # path('create', api_create_record_view, name="create"),



    path('courses/list', ApiscourseSerializerListView.as_view(), name="list"),





]