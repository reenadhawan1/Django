from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^travels/$', views.dashboard),
    url(r'^addtrip/$', views.addTrip),
    url(r'^tripadd/$', views.tripAdd),
    url(r'^trip/(?P<id>\d+)/$', views.trip),
    url(r'^cancel/(?P<id>\d+)/$', views.cancel),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
    url(r'^join/(?P<id>\d+)/$', views.join),
]