from django.contrib import admin

from scholarships.models import(
     Universitie,
     Scholarship,
     Tag,
    #  Job,
     Guide,
    
  )


admin.site.register(Universitie)
admin.site.register(Scholarship)
admin.site.register(Tag)
# admin.site.register(Job)
admin.site.register(Guide)

