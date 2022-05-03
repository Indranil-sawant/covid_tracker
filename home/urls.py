from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home , name='home'),
    
    path('sec/', views.search, name='sec'),
    
    path('voice/', views.index , name='index'),
     

]