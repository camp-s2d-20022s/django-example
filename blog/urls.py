from django.http import HttpRequest, HttpResponse
from django.urls import include, path

def blog(req):
    return HttpResponse('blog')

urlpatterns = [
    path('', blog)
]
