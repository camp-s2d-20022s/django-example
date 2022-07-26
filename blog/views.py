from django.http import HttpRequest, HttpResponse, JsonResponse
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

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json

@csrf_exempt
def api_post_list(req):
    if req.method == 'GET':
        posts = models.Post.objects.all()
        return JsonResponse({"results": list(posts.values())})
    elif req.method == 'POST':
        body = json.loads(req.body.decode('utf-8'))
        p = models.Post(title=body['title'], content=body['content'])
        p.save()
        return JsonResponse({"results": model_to_dict(p)})
    else:
        return HttpResponse(status=405)

@csrf_exempt
def api_post(req, pk):
    if req.method == 'GET':
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return HttpResponse(status=404)
        return JsonResponse({"results": model_to_dict(post[0])})
    elif req.method == 'PUT':
        body = json.loads(req.body.decode('utf-8'))
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return HttpResponse(status=404)
        p = post[0]
        p.title = body['title']
        p.content = body['content']
        p.save()
        return JsonResponse({"results": model_to_dict(p)})
    elif req.method == 'DELETE':
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return HttpResponse(status=404)
        p = post[0]
        p.delete()
        return JsonResponse({"results": "ok"})
    else:
        return HttpResponse(status=405)