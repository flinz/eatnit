from django.contrib import admin
from django.conf.urls import patterns, include, url

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
# hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
    '',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Login and user admin
    url(r'^accounts/', include('allauth.urls')),
 	
 	# Eatnit.com specific 
    url(r'^', include('eatnit.apps.food.urls')),
       
)
