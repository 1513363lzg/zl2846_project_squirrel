from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv, datetime
from django.apps import apps

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)


    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, mode='w') as csvfile:
            names = ['Latitude', 'Longitude', 'Unique_squirrel_ID','Hectare','Shift', 'Date', 'Age', 'Primary_fur_color', 'Location',
                        'Specific_location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(names)
            for i in Squirrel.objects.all():
                writer.writerow([getattr(i, name) for name in names])
