from django.contrib import admin

from countries.models import(
    Country_details,
)

class Country_detailsAdmin(admin.ModelAdmin):
        search_fields = ('country_name','country_code','phone_code')
        list_display = ('country_name', 'country_code','phone_code')

admin.site.register(Country_details,Country_detailsAdmin)


