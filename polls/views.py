from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ctx = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', ctx)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {
        'question': question,
    }
    return render(request, 'polls/detail.html', ctx)

def results(request, question_id):
    response = "Results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s" % question_id)
