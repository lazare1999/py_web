"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
]
