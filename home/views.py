
from ast import Global
from itertools import count
from django.shortcuts import render
from django.http import HttpResponse as HT
import requests
from home.models  import Data




def index(request):
    r = requests.get('https://api.covid19api.com/summary')
    all = r.json()["Global"]
    primary_data = r.json()["Countries"]
    return render(request, 'index.html', {'all':all,
    'primary_data': primary_data,})
   

def sec(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        return render(request , 'search.html' , {'searched':searched})
 

def search(request):
    all_countries = {}
    if 'searched' in request.GET:
        country_name = request.GET['searched']
        url = 'https://api.covid19api.com/summary'%country_name 
        response = requests.get(url)
        data = response.json()
        list_countries = data['Countries']

        for c in list_countries:
            country_data = Data(
                 name = c['Country'],
                 country_code =c['CountryCode'],
                 new_confirmed = c['NewConfirmed'],
                 total_confirmed =c['TotalConfirmed'],
                 new_deaths =c['NewDeaths'],
                 total_deaths = c['TotalDeaths'],
                 new_recovered = c['NewRecovered'],
                 total_recovered = c['TotalRecovered'],
                 date =c['Date'],
            )
            country_data.save()
            all_countries = Data.objects.all().order_by('name')
    return render (request , 'index.html', {'all_countries':all_countries})
        
def home(request):
    return render(request, 'homepage.html')



