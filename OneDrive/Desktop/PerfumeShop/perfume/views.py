from django.shortcuts import render
from django.http import HttpResponse
from .models import Perfume 


def home (request):
    perfume = Perfume.objects.all()
    return render(request, 'home.html', {'perfume': perfume})
 