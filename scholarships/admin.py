from django.contrib import admin

from scholarships.models import(
     University,
     Scholarship,
     Tag,
     Job,
     Guide,
    
  )


admin.site.register(University)
admin.site.register(Scholarship)
admin.site.register(Tag)
admin.site.register(Job)
admin.site.register(Guide)

