# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world. Here is the polls index.")


def detail(request, question_id):
    return HttpResponse("You are looking at question {}".format(question_id))


def results(request, question_id):
    response = "You are looking at question %s -result-"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are looking at question %s. -vote-" % question_id)
