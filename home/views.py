
from ast import Global
from itertools import count
from django.shortcuts import render
from django.http import HttpResponse as HT
import requests





def index(request):
    r = requests.get('https://api.covid19api.com/summary')
    all = r.json()["Global"]
    country = r.json()["Countries"]
    return render(request, 'index.html', {'all':all,
    'country': country,})
   

def sec(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        return render(request , 'search.html' , {'searched':searched})
 
