"""This module contains views."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import F

from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    """Index view of polls."""

    template_name = 'polls/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """Detail view of polls."""

    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    """Results view of polls."""

    model = Question
    template_name = "polls/results.html"


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
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
