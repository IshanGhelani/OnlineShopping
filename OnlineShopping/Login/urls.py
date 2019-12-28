from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url('create/', TemplateView.as_view(template_name='create.html', content_type='text/html')),
    url('create/', views.create),
    url('forgott/', views.forgott),
    url('forgot/', views.forgot),
    url('register/', views.register),
    url('verifyt/', views.verifyt),
    url('logout/', views.logout),
    url('verify/', views.verify),
    url('change/', views.change),
    url('profile/', views.profile),
    url('updatet/', views.updatet),
    url('update/', views.update),
    url('', views.login),
]

'''try:
    x = request.session['id']
except KeyError:
    return render(request, 'login.html', {'msg': 'Login to view bill !'})'''
