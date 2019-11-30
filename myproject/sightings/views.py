
from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel
def index(request):
    Squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': Squirrels,
            }
    return render(request, 'sightings/all.html', context)

def add_squirrel(request,Squirrel_id):
    pet = Squirrel.objects.get(id=Squirrel_id)
    return HttpResponse(pet.Age)


def all_squirrels(request,Squirrel_id):
    pet = Squirrel.objects.get(id=Squirrel_id)
    return HttpResponse(pet.Age)


def squirrel_details(request,Squirrel_id):
    pet = Squirrel.objects.get(id=pet_id)
    return HttpResponse(pet.Age)





