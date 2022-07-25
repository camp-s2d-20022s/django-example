from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

def index(req:HttpRequest) -> HttpResponse:
    print(req.user, req.user.email, req.user.last_login)
    latest_question_list = models.Question.objects.order_by('-publish_date')[:5]

    if req.session.get('count') is None:
        req.session['count'] = 0
    req.session['count'] += 1
    print(req.session['count'])

    res = render(req, 'polls/index.html', {'latest_question_list': latest_question_list})
    res.set_cookie('univ', 'hgu')
    return res

def detail(req, question_id):
    print(req.COOKIES['univ'])
    print(req.session['count'])
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = models.Question.objects.filter(pk=question_id)
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