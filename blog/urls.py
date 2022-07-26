from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index),
    path('post_list/', views.post_list, name="list"),
    path('post_detail/<int:pk>/', views.post_detail, name="detail"),
    path('post_create/', views.post_create, name="create"),
    
    path('api/post/', views.api_post_list, name="api_list"),
    path('api/post/<int:pk>/', views.api_post, name="api_one")
]

# from django.views.generic import ListView
# from . import models

# urlpatterns = [
#     path('', views.index),
#     path('post_list', ListView.as_view(model=models.Post))
# ]