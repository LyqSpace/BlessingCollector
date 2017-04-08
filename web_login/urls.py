from django.conf.urls import url

from web_login import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]