from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about me",
        "this_is_true":True,
        "number": 34,
        "list":[34,67,89,312,'abc'],
        "my_html":"<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)