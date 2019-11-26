from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .model import Squirrel
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'map/detail.html', {'question': question})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
