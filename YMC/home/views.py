from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeImages



def home(request):
    imgs = HomeImages.objects.all()
    # event = events.objects.all()
    return render(request, 'home/index.html', {'imgs':imgs})
