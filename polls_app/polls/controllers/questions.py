from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from ..models import *

def new(request):
    string = "string"
    return render(request, 'polls/new.html', {"string": string})

def create_question(request):
    try:
        new_question = Question(question_text=request.POST['question_text'], pub_date= timezone.now())
        new_question.save()
    except:
        return render('polls/new.html', {
            'error_message': "Something went wrong",
        })
    else:
        return HttpResponseRedirect(reverse('polls:detail', args=(new_question.id,)))
