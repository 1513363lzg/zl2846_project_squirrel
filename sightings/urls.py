from django.urls import path
  
from . import views

urlpatterns =[
        path('', views.index),
        path('stats/', views.squirrel_stats),
        path('add/',views.add_squirrel, name='add'),
        path('<str:sq_id>/', views.edit_squirrel,name='edit'),
        ]

