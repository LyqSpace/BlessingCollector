from django.conf.urls import url

from web_user_management import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_new_user/$', views.create_new_user, name='create_new_user'),
    url(r'^select_old_user/$', views.select_old_user, name='select_old_user'),
    url(r'^update_user_info/$', views.update_user_info, name='update_user_info'),
]