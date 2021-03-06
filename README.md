<div align="center">
<img src="https://img.icons8.com/color/100/000000/squirrel.png">
</div>

# Squirrel Tracking Application 
### author: Zhigeng (casper) Liu, Zhuoran Li UNIs: [zl2846, zl2838]  Project Group 28, Section 2
# Overview
Based on 2018 Central Park Squirrel Census data, Squirrel Tracking Application can realize keeping track of all the known squirrel in the Central Park.

# Dataset
<a href="https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw">2018 Central Park Squirrel Census.</a> 
 On this page, click API and choose .csv file changes the name and copy link. 
```sh
# get dataset on your local repo
wget https://data.cityofnewyork.us/resource/import_squirrel_data.csv
```
 - Hint: if you use this way to import data, the columns of .CSV may be a littel different(lowercase). So if you use other ways to import data, please change /sightigns/models.py file to match with keys of data from .csv.
 
# Preparation 
```sh
# Terminal, Django is a framework  need to install
pip install django 
```
```sh
# Terminal
django-admin startproject project 
```
```sh
# Terminal
python manage.py startapp yourapp
```

# Applications
## Map

**-browsing all squirrel sightings**

   -Located at: /map

   -description: It shows a map that displays the location of the squirrel sightings. Therefore, it allows users to keep track of all the known squirrels in the Central Park.


## Sightings

 **-browsing all squirrel sightings**
   
-Located at: /sightings
  
 -description: It is the home page of sightings. Users have access to information about all squirrel sightings in the central park.


 **-editing existing squirrel sightings**
   
-Located at: /sightings/<unique-squirrel-id>
   
-description: Users are allowed to click any unique squirrel id on the home page of sightings to link to edit interface. Users are able to update any attribute of the squirrel sighting.


 **-creating squirrel sightings**
   
-Located at: /sightings/add
   
-description: Users can click the button ‘Add Sighting’ on the top of home page of sightings to link to add page. It allows users to add the new squirrel sighting by themselves.


**-viewing general stats of squirrel sightings**
   
-Located at: /sightings/stats
   
-description: Users can click the button ‘Stats Sighting’ on the top of home page of sightings to link to stats page. It provides the stats of five attributes.

# The link to the server running our application
 - To view 100 squirrels in Map https://sylvan-airship-253800.appspot.com/map
 - To view Each Squirrel detail information https://sylvan-airship-253800.appspot.com/sightings

# Group Information
Project Group 28, Section 2

# Group Members
Zhigeng (casper) Liu, Zhuoran Li
UNIs: [zl2846, zl2838]

