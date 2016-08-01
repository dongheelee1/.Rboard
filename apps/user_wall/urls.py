# Inside apps/appname/urls.py might look like this:
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index")
]