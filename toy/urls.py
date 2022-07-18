from django.urls import path
from . import views

urlpatterns = [
    path('gugu/<int:num>/', views.gugu)
]
