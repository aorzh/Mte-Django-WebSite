# Create your views here.
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
#from django.views.generic import object_detail
#from django.views.generic import ListView
#from palaiseo import views
from sito import views
#from blog.views import PageView
from sito.views import HomeView, PaginaView
from sito.models import Page
#from blog.models import Pagine
#from django.contrib.syndication.views import Feed

urlpatterns = patterns('blog.views',
   url(r'^$', HomeView.as_view()),
   url(r'^(?P<pk>\d+)/$', PaginaView.as_view()),
   #url(r'^([-_A-Za-z0-9]+)/$', views.dettaglio),
   #url(r'^pagine/(?P<pk>\d+)/$', PageView.as_view()),
  )
