from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from . import models

def index(req:HttpRequest) -> HttpResponse:
    latest_question_list = models.Question.objects.filter(publish_date__lt=timezone.now()).order_by('-publish_date')[:5]
    res = render(req, 'polls/index.html', {'latest_question_list': latest_question_list})
    return res

def detail(req, question_id):
    question = models.Question.objects.filter(pk=question_id, publish_date__lt=timezone.now())
    if len(question) == 0:
        raise Http404("Question does not exist")
    return render(req, 'polls/detail.html', {'question': question[0]})

def results(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))