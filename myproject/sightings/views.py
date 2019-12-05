from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms
from .forms import SquirrelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Squirrel
def index(request):
    Squirrels = Squirrel.objects.all()
    context = {
            'Squirrels': Squirrels,
            }
    return render(request, 'sightings/all.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()

    context = {
            'form': form,
    }
    return render(request, 'sightings/edit.html', context)

def all_squirrels(request):
    return HttpResponse('list all squirrels information')

def squirrel_details(request,Unique_squirrel_ID):
    pet = Squirrel.objects.get(id=Unique_squirrel_ID)
    return HttpResponse({'Age: %a' %pet.Age,' Date: %a' %pet.Date})

def squirrel_details(request,Unique_squirrel_ID):
    a = Squirrel.objects.get(id=Unique_squirrel_ID)
    if request.method =="POST":
        a.delete()
        return redirect('index')

def squirrel_stats(request):
    sightings_stats1=Squirrel.objects.all().count()
    sightings_stats2=Squirrel.objects.filter(Primary_fur_color='Black').count()
    sightings_stats3=Squirrel.objects.filter(Primary_fur_color='Gray').count()
    sightings_stats4=Squirrel.objects.filter(Age='Adult').count()
    sightings_stats5=Squirrel.objects.filter(Age='Juvenile').count()
    context={'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)


def edit_pet(request,pet_id):
    pet=Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST,instance=pet)
    # check data with form 
        if form.is_valid():
            form.save()
            return redirect(f'sightings/{pet_id}')
    else:
        form = SquirrelForm(instance=pet)
        context ={
                'form':form,
            }
    return render (request,'sightings/edit.html',context)

