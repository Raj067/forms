from django.shortcuts import render

# Create your views here.

def hello(request, *args, **kwargs):
    return render(request, "home.html", {})
