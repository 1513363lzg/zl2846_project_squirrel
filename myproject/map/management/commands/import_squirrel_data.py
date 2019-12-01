from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel as S
import pandas as pd 
import os

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
        # Positional arguments
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        a=pd.read_csv(os.getcwd()+options['file_path'])
        column=a.columns
        for i in range(len(a)):
            p=S(
                Latitude=a.iloc[i]['y'],
                Longitude=a.iloc[i]['x'],
                Unique_squirrel_ID=a.iloc[i][column[2]],
               Hectare=a.iloc[i][column[3]],
                Shift=a.iloc[i][column[4]],
    Date=a.iloc[i][column[5]]    ,
    Hectare_squirrel_num=a.iloc[i][column[6]],    
    Age=a.iloc[i][column[7]],
    Primary_fur_color=a.iloc[i][column[8]],        
    Location=a.iloc[i]['location'],    
    Specific_location=a.iloc[i][column[14]],
    Running=a.iloc[i]['running'],    
    Chasing=a.iloc[i]['chasing'],   
    Climbing=a.iloc[i]['climbing'],    
    Eating=a.iloc[i]['eating'],
    Foraging=a.iloc[i]['foraging'],
    Other_Activities=a.iloc[i]['other_activities'],
    Kuks=a.iloc[i]['kuks'],    
    Quaas=a.iloc[i]['quaas'],    
    Moans=a.iloc[i]['moans'],    
    Tail_flags=a.iloc[i]['tail_flags'],    
    Tail_twitches=a.iloc[i]['tail_twitches'],
    Approaches=a.iloc[i]['approaches'],    
    Indifferent =a.iloc[i]['indifferent'],   
    Runs_from =a.iloc[i]['runs_from'],   
    )
            p.save()        


