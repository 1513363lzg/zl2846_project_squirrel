from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms

from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel
def index(request):
    Squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': Squirrels,
            }
    return render(request, 'sightings/all.html', context)

def add_squirrel(request):
    return HttpResponse('we need to create a new html for edit')

#just an example
def all_squirrels(request):
    return HttpResponse('list all squirrels information')

def squirrel_details(request, Squirrel_id):
    pet = Squirrel.objects.get(id=Squirrel_id)
    return HttpResponse({'Age: %a' %pet.Age,' Date: %a' %pet.Date})

def squirrel_stats(request):
    sightings_stats1=Squirrel.object.all().count()
    sightings_stats2=Squirrel.object.filter(PRIMARYFURCOLOR_CHOICES='Black').count()
    sightings_stats3=Squirrel.object.filter(PRIMARYFURCOLOR_CHOICES='Gray').count()
    sightings_stats4=Squirrel.object.filter(Age='Adult').count()
    sightings_stats5=Squirrel.object.filter(Age='Juvenile').count()
    context={'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)

