from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from . import models
from . import forms

def index(req: HttpRequest) -> HttpResponse:
    return HttpResponse('blog')

def post_list(req):
    posts = models.Post.objects.all()
    return render(req, 'blog/post_list.html', {"post_list": posts})

def post_detail(req, pk):
    post = models.Post.objects.get(pk=pk)
    return render(req, 'blog/post_detail.html', {"post": post})

def post_create(req):
    if req.method == "POST":
        form = forms.PostModelForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/blog/post_list/")
    else:
        form = forms.PostForm()
    
    return render(req, 'blog/post_create.html', {'form': form})

def api_post(req):
    return HttpResponse("json")