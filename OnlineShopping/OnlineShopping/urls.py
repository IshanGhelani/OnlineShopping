from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('About/', include("About.urls")),
    url('Cart/', include("Cart.urls")),
    url('Contact/', include("Contact.urls")),
    url('Login/', include("Login.urls")),
    #url('Home/', include("Home.urls")),
    url('', include("Home.urls")),
]
