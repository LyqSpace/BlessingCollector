from django.conf.urls import url

from web_home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_blessing/$', views.save_blessing, name='save_blessing')
]