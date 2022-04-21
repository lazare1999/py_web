"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),
    path(r'^topics/$', views.topics, name='topics'),

    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    path(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    path(r'^car_brands/$', views.car_brands, name='car_brands'),

    path(r'^car_brands/(?P<brand_id>\d+)/$', views.brand, name='brand'),

    path(r'^new_brand/$', views.new_brand, name='new_brand'),

    # Page for adding a new entry
    path(r'^new_car/(?P<brand_id>\d+)/$', views.new_car, name='new_car'),

    # Page for editing an entry
    path(r'^edit_car/(?P<car_id>\d+)/$', views.edit_car, name='edit_car'),
]
