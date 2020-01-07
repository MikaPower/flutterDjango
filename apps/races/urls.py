from django.conf.urls import url
from django.urls import path

import apps
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[-\w]+)/$', views.get_post_race, name='race-name'),
    url(r'^(?P<id>[-\w]+)/pilots$', views.get_pilots_race, name='race-name'),

]