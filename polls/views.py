from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse("polls")

def detail(req, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(req, question_id):
    response = "You're looking at the results of question {0}. {1} {0}"
    return HttpResponse(response.format(question_id, "aaa"))

def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")