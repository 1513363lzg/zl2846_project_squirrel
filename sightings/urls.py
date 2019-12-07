from django.urls import path
  
from . import views

urlpatterns =[
        path('', views.index),
        path('stats/', views.squirrel_stats),
        path('<int:Unique_squirrel_ID>/', views.edit_squirrel),
        path('add/',views.add_squirrel, name='add'),
        ]

