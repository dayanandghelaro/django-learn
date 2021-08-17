"""This module contains views."""
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice


# Create your views here.
def index(request):
    """Show default homepage."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """Detail of question."""
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    """Show result of votes."""
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    """Vote any question."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
