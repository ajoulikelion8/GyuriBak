from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Profile
# Create your views here.

def main(request):
    profile = Profile.objects.last()
    if 'submit' in request.GET:
        profile= Profile()
        profile.name=request.GET['name']
        profile.body = request.GET['body']
        profile.save()
    return render(request,'content/main.html',{'profile':profile})

def pfedit(request):
    return render(request,'content/pfedit.html')
