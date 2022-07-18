from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(req):
    return HttpResponse('blog')

def post_list(req):
    posts = models.Post.objects.all()
    return render(req, 'blog/post_list.html', {"post_list": posts})