from django.shortcuts import render
from django.http import HttpResponse

#App1

# Create your views here.

def f11(request):
    return HttpResponse("<h2>Hello user...!! Have a nice day</h2><hr/>")