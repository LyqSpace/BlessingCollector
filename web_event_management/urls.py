from django.conf.urls import url

from web_event_management import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]