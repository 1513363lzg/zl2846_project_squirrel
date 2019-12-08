from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django import forms
from .forms import SquirrelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Squirrel
def index(request):
    
    squirrels = Squirrel.objects.all()
    fields = ['Unique_Squirrel_ID','Date','Latitude','Longitude','Hectare','Age','Primary_fur_color','Location','Specific_location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_Flags','Tail_Twitches','Approaches','Indifferent','Runs_From']
    context={
        'squirrels':squirrels,
        'fields':fields,
    }    
    return render(request,'sightings/all.html',context)



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

def add_squirrel(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm()
    return render(request, 'sightings/edit.html', {'form':form})

def edit_squirrel(request,sq_id):
    instance = get_object_or_404(Squirrel, Unique_squirrel_ID=sq_id)
    form = SquirrelForm(request.POST or None,instance=instance)
    # check data with form
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/')
    else:
        context ={
                'form':form,
                'Unique_squirrel_ID':sq_id,
            }
    return render (request,'sightings/edit.html',context)

