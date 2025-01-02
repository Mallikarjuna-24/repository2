from django.shortcuts import render
from django.http import HttpResponse

#MultiViewApp

# Create your views here.

def f1(request):
    return HttpResponse("<center><h1>Good Morning User..!! Have a nice day</h1></center>")
    
def f2(request):
    return HttpResponse("<center><h1>Good Afternoon User..!! Hope you doing good</h1></center>")

def f3(request):
    return HttpResponse("<center><h1>Good Evening User..!! How was your day</h1></center>")
