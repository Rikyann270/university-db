from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Schola Administration'

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    
    #rest_framework urls

    # account
    path('api/accounts/', include('accounts.api.urls', 'accounts_api')),

    #other
    path('api/scholarships/', include('scholarships.api.urls', 'scholarships_api')),
    path('api/courses/', include('courses.api.urls', 'courses_api')),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
