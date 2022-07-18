from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse('blog')

def post_list(req):
    posts = [
        {'pk': 1, 'title': 'html', 'content': 'html is ...'},
        {'pk': 2, 'title': 'css', 'content': 'css is ...'},
        {'pk': 3, 'title': 'javascipt', 'content': 'javascipt is ...'},
        {'pk': 4, 'title': 'python', 'content': 'python is ...'},
        {'pk': 5, 'title': 'django', 'content': 'django is ...'},
    ]

    return render(req, 'blog/post_list.html')