from django.urls import path

from scholarships.api.views import (
    # single
    api_scholarship_detail_view,
    #list
    ApischolarshipsListView,
    ApistagSerializerListView,
    ApiguideSerializerListView,
    ApiuniversitySerializerListView,
    Apisubmitted_scholarshipListView,

    # searching
    Apischolarships_degree_ListView,
    Apischolarships_subject_ListView,
    Apischolarships_eligibity_ListView,
    Apischolarships_country_ListView,
    Apischolarships_closing_date_ListView,



    )

app_name = 'scholarships'

urlpatterns = [
    path('<slug>/', api_scholarship_detail_view, name="detail"),
    # path('create', api_create_record_view, name="create"),


    #main search
    path('scholarship/list', ApischolarshipsListView.as_view(), name="list"),
    # searching attr
    path('degree/list', Apischolarships_degree_ListView.as_view(), name="list"),
    path('subject/list', Apischolarships_subject_ListView.as_view(), name="list"),
    path('eligibity/list', Apischolarships_eligibity_ListView.as_view(), name="list"),
    path('country/list', Apischolarships_country_ListView.as_view(), name="list"),
    path('closing_date/list', Apischolarships_closing_date_ListView.as_view(), name="list"),


    path('tags/list', ApistagSerializerListView.as_view(), name="list"),
    # path('jobs/list', ApijobSerializerListView.as_view(), name="list"),
    path('guides/list', ApiguideSerializerListView.as_view(), name="list"),
    path('universities/list', ApiuniversitySerializerListView.as_view(), name="list"),
    path('submitted_scholarship/list', Apisubmitted_scholarshipListView.as_view(), name="list"),



]