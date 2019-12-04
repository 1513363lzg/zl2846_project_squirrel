from django.urls import path
  
from . import views

urlpatterns =[
        path('', views.index),
        path('add/', views.add_squirrel),
        path('stats/', views.squirrel_stats),
        path('<int:Squirrel_id>/', views.squirrel_details),
        ]

