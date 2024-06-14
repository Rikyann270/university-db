from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe 




from assets.models import(
     Main_image,
     Featured_image,
 
  )


class Main_imageAdmin(admin.ModelAdmin):

    readonly_fields = ('Main_image_preview',)  # Make the image preview field read-only

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Check if it's a new scholarship object
            form.base_fields['main_image']
        return form

    def Main_image_preview(self, obj):
        if obj.main_image:
            return mark_safe('<img src="{url}" style="border-radius:5px;" width="150px" height="auto" />'.format(url=obj.main_image.url))
        # else:
            # return mark_safe('<img src="{url}" style="border-radius:5px;" width="150px" height="auto" />'.format(url=obj.Main_image.url))
        

    Main_image_preview.short_description = 'Image preview'


class Featured_imageAdmin(admin.ModelAdmin):

    readonly_fields = ('Featured_image_preview',)  # Make the image preview field read-only

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Check if it's a new scholarship object
            form.base_fields['featured_image']
        return form

    def Featured_image_preview(self, obj):
        if obj.featured_image:
            return mark_safe('<img src="{url}" style="border-radius:5px;" width="150px" height="auto" />'.format(url=obj.featured_image.url))
        # else:
            # return mark_safe('<img src="{url}" style="border-radius:5px;" width="150px" height="auto" />'.format(url=obj.Main_image.url))
        

    Featured_image_preview.short_description = 'Image preview'


admin.site.register(Main_image,Main_imageAdmin)
admin.site.register(Featured_image,Featured_imageAdmin)


