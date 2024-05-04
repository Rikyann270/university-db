from django.contrib import admin

from scholarships.models import(
     Universitie,
     Scholarship,
     submitted_scholarship,
     Tag,
    Degree,
     Guide,
    
  )


admin.site.register(Universitie)
admin.site.register(Scholarship)
admin.site.register(submitted_scholarship)
admin.site.register(Tag)
admin.site.register(Degree)
admin.site.register(Guide)

