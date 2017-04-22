from django.conf.urls import url

from web_event_management import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_birthday/$', views.add_birthday, name='add_birthday'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^delete_event/$', views.delete_event, name='delete_event'),
    url(r'^arrange_blessings/$', views.arrange_blessings, name='arrange_blessings'),
]