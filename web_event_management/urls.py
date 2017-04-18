from django.conf.urls import url

from web_event_management import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_birthday/$', views.add_birthday, name='add_birthday')
]