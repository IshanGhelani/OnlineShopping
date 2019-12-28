from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url('payment/', views.pay),
    url('bill/', views.bill),
    url('add/', views.add),
    url('remove/', views.remove),
    url('place/', views.place),
    url('history/', views.history),
    url('', views.cart),
]