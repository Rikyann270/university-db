from django.urls import path,include
from rest_framework.routers import DefaultRouter

from scholarships.api.views import (
    # single
    api_scholarship_detail_view,
    #list
    ApischolarshipsListView,
    ApistagSerializerListView,
    ApiguideSerializerListView,
    ApiuniversitySerializerListView,
    Apisubmitted_scholarshipListView,

    # University_country_Serializer
    Api_University_country_SerializerListView,

    # searching

    # filter_multile
    ApischolarshipViewSet



    )

app_name = 'scholarships'

router = DefaultRouter()
router.register(r'scholarships', ApischolarshipViewSet)

urlpatterns = [
     path('filter/', include(router.urls)),
    #  http://127.0.0.1:8000/api/scholarships/filter/scholarships?degree=phd&funding_status=Fully funded
    path('<slug>/', api_scholarship_detail_view, name="detail"),
    # path('create', api_create_record_view, name="create"),


    #main search
    path('scholarship/list', ApischolarshipsListView.as_view(), name="list"),
    # main 2
    # path('scholarship2/list', ApischolarshipsListView22.as_view(), name="scholarship2"),
    # searching attr

    path('tags/list', ApistagSerializerListView.as_view(), name="list"),
    # path('jobs/list', ApijobSerializerListView.as_view(), name="list"),
    path('guides/list', ApiguideSerializerListView.as_view(), name="list"),
    path('universities/list', ApiuniversitySerializerListView.as_view(), name="list"),
    path('submitted_scholarship/list', Apisubmitted_scholarshipListView.as_view(), name="list"),
    path('university_country/list', Api_University_country_SerializerListView.as_view(), name="list"),



]