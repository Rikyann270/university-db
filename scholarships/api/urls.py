from django.urls import path

from scholarships.api.views import (
    api_scholarship_detail_view,
    ApischolarshipsListView,
    ApistagSerializerListView,
    # ApijobSerializerListView,
    ApiguideSerializerListView,
    ApiuniversitySerializerListView,


    )

app_name = 'scholarships'

urlpatterns = [
    path('<slug>/', api_scholarship_detail_view, name="detail"),
    # path('create', api_create_record_view, name="create"),



    path('scholarship/list', ApischolarshipsListView.as_view(), name="list"),
    path('tags/list', ApistagSerializerListView.as_view(), name="list"),
    # path('jobs/list', ApijobSerializerListView.as_view(), name="list"),
    path('guides/list', ApiguideSerializerListView.as_view(), name="list"),
    path('universities/list', ApiuniversitySerializerListView.as_view(), name="list"),



]