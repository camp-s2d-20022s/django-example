from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_list', views.post_list),
    path('post_detail/<int:pk>/', views.post_detail)
]

# from django.views.generic import ListView
# from . import models

# urlpatterns = [
#     path('', views.index),
#     path('post_list', ListView.as_view(model=models.Post))
# ]