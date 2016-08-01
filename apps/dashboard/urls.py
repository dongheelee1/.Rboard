# Inside apps/appname/urls.py might look like this:
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^edit/(?P<user_id>\d+)/$', views.show_admin_edit, name="show_admin_edit"), 
    url(r'^admin_update_status/(?P<user_id>\d+)/$', views.admin_update_status, name="admin_update_status"),
   	url(r'^admin_update_password/(?P<user_id>\d+)/$', views.admin_update_password, name="admin_update_password"),
   	url(r'^user_update_password/(?P<my_id>\d+)/$', views.user_update_password, name="user_update_password"),
   	url(r'^user_update_profile/(?P<my_id>\d+)/$', views.update_profile, name="user_update_profile"),
   	url(r'^user_update_description/(?P<my_id>\d+)/$', views.update_description, name="user_update_description"),
   	url(r'^delete_user/(?P<user_id>\d+)/$', views.delete_user, name="delete_user"),
   	url(r'^add_user/$', views.show_add_user, name="show_add_user"),
   	url(r'^profile/$', views.show_user_profile, name="show_user_profile"),  
   	url(r'^create/$', views.create_user, name="create_user"),  
]