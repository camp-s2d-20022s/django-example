from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('posts/', views.PostList.as_view(), name="post-list"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
