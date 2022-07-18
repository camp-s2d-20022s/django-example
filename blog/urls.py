from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_list', views.post_list)
]

# from django.views.generic import ListView
# from . import models

# urlpatterns = [
#     path('', views.index),
#     path('post_list', ListView.as_view(model=models.Post))
# ]