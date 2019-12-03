from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
class Delete(DeleteView):
    model = Squirrel
    success_url = reverse_lazy('')

def all_squirrels(request):
    return HttpResponse('list all squirrels information')

def squirrel_details(request, Squirrel_id):
    pet = Squirrel.objects.get(id=Squirrel_id)
    return HttpResponse({'Age: %a' %pet.Age,' Date: %a' %pet.Date})




