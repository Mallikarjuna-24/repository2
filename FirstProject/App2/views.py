from django.shortcuts import render
from django.http import HttpResponse
import datetime

#App2

# Create your views here.

def f22(request):
    time=datetime.datetime.now()
    msg="<h2>Hello user..!<br/><br/>date & time: ",time,"</h2><hr/>"
    return HttpResponse(msg)