from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    
    path('sec/', views.search, name='sec'),

    path('home/', views.home , name='home'),
     

]