from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe 



from scholarships.models import(
     Universitie,
     Scholarship,
     submitted_scholarship,
     Tag,
    Degree,
     Guide,
    
  )







class UniversitieAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country')
    # ordering = ('name',)
    list_filter = ('country',)
    list_per_page=100

    fieldsets = (
          (None, {
              'fields': ('name', 'country','University_image',)
          }),
          ('Additional Information', {
              'fields': ('domain1', 'domain2', 'domain3','domain4','webpage1', 'webpage2','webpage3','webpage4',
                         'alpha_two_code','state_province'),
              'classes': ('collapse',)
          }),
    )




class ScholarshipAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country', 'University_name')
    # ordering = ('name',)
    # list_filter = ('country',)
    list_filter = ('closing_date','country',)
    list_per_page=100

    list_display = ('name', )  # Display a preview of the image in the admin list view
    # readonly_fields = ('Scholarship_image_preview',)  # Make the image preview field read-only

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if not obj:  # Check if it's a new scholarship object
    #         form.base_fields['Scholarship_image'].initial = default_image_path
    #     return form

    # def Scholarship_image_preview(self, obj):
    #     if obj.Scholarship_image:
    #         return mark_safe('<img src="{url}" width="100px" height="auto" />'.format(url=obj.Scholarship_image.url))
    #     else:
    #         return mark_safe('<img src="{url}" width="100px" height="auto" />'.format(url=obj.default_image_path))

    # Scholarship_image_preview.short_description = 'Scholarship Image'  # Set a custom column header for the image preview







admin.site.register(Universitie,UniversitieAdmin)
admin.site.register(Scholarship,ScholarshipAdmin)
admin.site.register(submitted_scholarship)
admin.site.register(Tag)
admin.site.register(Degree)
admin.site.register(Guide)

