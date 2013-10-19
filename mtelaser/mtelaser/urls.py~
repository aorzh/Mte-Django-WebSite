from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtelaser.views.home', name='home'),
    url(r'^', include('sito.urls')),
    # url(r'^mtelaser/', include('mtelaser.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/posts', include(admin.site.urls)),
    #url(r'^admin/pages', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
 )




if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^sito/media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
          )  

