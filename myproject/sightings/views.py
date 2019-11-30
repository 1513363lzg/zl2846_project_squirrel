
from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel
def index(request):
    Squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': Squirrels,
            }
    return render(request, 'sightings/all.html', context)

def add_squirrel(request,Unique_squirrel_ID):
    pet = Squirrel.objects.get(id=Unique_squirrel_ID)
    return HttpResponse(pet.Age)


def all_squirrels(request,Unique_squirrel_ID):
    pet = Squirrel.objects.get(id=Unique_squirrel_ID)
    return HttpResponse(pet.Age)

def squirrel_details(request, Squirrel_id):
    pet = Squirrel.objects.get(id=Squirrel_id)
    return HttpResponse({'Age: %a' %pet.Age,' Date: %a' %pet.Date})




