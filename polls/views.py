from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from . import models

def index(req:HttpRequest) -> HttpResponse:
    latest_question_list = models.Question.objects.order_by('-publish_date')[:5]
    return render(req, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(req, question_id):
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = models.Question.objects.filter(pk=question_id)
    if len(question) == 0:
        raise Http404("Question does not exist")
    return render(req, 'polls/detail.html', {'question': question[0]})

def results(req, question_id):
    response = "You're looking at the results of question {0}. {1} {0}"
    return HttpResponse(response.format(question_id, "aaa"))

def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
