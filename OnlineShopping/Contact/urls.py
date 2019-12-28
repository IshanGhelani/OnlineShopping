from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url('feedback/', views.feed),
    #url('', TemplateView.as_view(template_name='contact.html', content_type='text/html')),
    url('', views.cont)
]