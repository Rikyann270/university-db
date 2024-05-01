from django.contrib import admin

from courses.models import(
    Course_detail,
    Subject,
)

admin.site.register(Course_detail)
admin.site.register(Subject)




