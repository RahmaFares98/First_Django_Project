from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),#http://localhost:8000
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<int:number>/', views.show),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/delete/', views.destroy),
    path('blogs/json/', views.blogs_json)  
]
