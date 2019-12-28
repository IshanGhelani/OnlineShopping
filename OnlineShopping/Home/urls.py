from django.conf.urls import url, include
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('Home/', TemplateView.as_view(template_name='index.html', content_type='text/html')),
    url('search/', views.search),
    url('showt/', views.showt),
    url('show/', views.show),
    url('view/', views.detail),
    #url('temp/', views.temp),
    url('', views.redirect),
]
