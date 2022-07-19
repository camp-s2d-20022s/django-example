from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse("polls")