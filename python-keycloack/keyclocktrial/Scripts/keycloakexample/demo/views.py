from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from demo.models import Site, Group, Search

# Create your views here.
def index(request):
    #return HttpResponse('You are the index. <a href="/secure">Secure</a>')
    return render(request, 'index.html')

def landing_page(request):
    site = Site.objects
    context = {'post':site}
    return render(request, "hom.html", context)

@login_required
def secure(request):
    return HttpResponse('Secure Page. <a href="/openid/logout">Logout</a>')

