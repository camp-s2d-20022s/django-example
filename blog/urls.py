from django.http import HttpRequest, HttpResponse
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('post_list', views.post_list)
]
