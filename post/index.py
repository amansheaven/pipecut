from django.shortcuts import reader
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello from post')