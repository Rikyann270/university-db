# filters.py
from django_filters import rest_framework as filters
from scholarships.models import(
    Scholarship,
    Tag,
    # Job,
    Guide,
    Universitie,
    submitted_scholarship,
    
)

class ScholarshipFilter_search(filters.FilterSet):
    degree = filters.CharFilter(field_name="degree", lookup_expr='icontains')
    country = filters.CharFilter(field_name="country", lookup_expr='icontains')
    # Add more filters as needed

    class Meta:
        model = Scholarship
        fields = ['degree', 'country']  # Add more fields as needed
