from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url('', TemplateView.as_view(template_name='description.html', content_type='text/html')),

]