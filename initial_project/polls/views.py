from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:]
    output = ", ".join([q.question_text for q in question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question: {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")

