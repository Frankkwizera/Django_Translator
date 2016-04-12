from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> HEY! AM BACK AGAIN</h1>')

def goo(request):
    return HttpResponse('Are we cool!!')
