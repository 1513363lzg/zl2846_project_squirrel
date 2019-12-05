from django.urls import path
  
from . import views

urlpatterns =[
        path('', views.index),
        path('stats/', views.squirrel_stats),
        path('<int:Unique_squirrel_ID>/', views.squirrel_details),
        path('<int:Unique_squirrel_ID>/edit/', views.edit_pet),
        
        ]

