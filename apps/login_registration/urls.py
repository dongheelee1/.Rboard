# Inside apps/appname/urls.py might look like this:
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login$', views.show_login, name='show_login'), 
    url(r'^register$', views.show_register, name='show_register'),
    url(r'^create_login$', views.create_login, name='create_login'), 
    url(r'^create_register$', views.create_register, name='create_register')
]