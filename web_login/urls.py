from django.conf.urls import url

from web_login import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_login/$', views.user_login, name='user_login')
]