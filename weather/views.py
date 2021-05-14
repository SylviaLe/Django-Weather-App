from django.shortcuts import render
import os
import requests
from .models import *
from .forms import *

KEY = os.environ['OPEN_WEATHER_API_KEY']

# Create your views here.
def index(request):
    ###preparing for the api call
    call = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='
    #remember the http at the beginning, or else you will have MissingSchema error
    url = call+KEY
    #####OPTION 1: Don't save to a database, start fresh
    form = CitiesForm()
    data = None   #initialize the var so that it wont give you an error
    msg = ''

    if request.method == "POST":
        form = CitiesForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['name']
            r = requests.get(url.format(city)).json()
            #print(r['cod'])

            if r['cod'] == 200:
                data = {
                    'city': city,  #it should be like this as you are getting the city name from the database, which was returned to you as objects
                    'temperature': r['main']['temp'], #the main is a dict
                    'description': r['weather'][0]['description'],  #weather is a list, so it need an int index first
                    'icon': r['weather'][0]['icon'], 
                }
            else:
                msg = 'City does not exist'


    #####OPTION 2: Save to a database, keep a list and extract the last value
    # if request.method == "POST":
    #     form = CitiesForm(request.POST)
    #     if form.is_valid():
            # new_city = form.cleaned_data['name']
            # existing_city = City.objects.filter(name=new_city).count()
            # if existing_city == 0:
    #           form.save() #this validate the form and save it at the same time
            # else:
            #     err_msg = 'City already exists' #then pass this as a context to render

    # ###make a form to take care of the input
    # form = CitiesForm()

    # ###requesting multiple cities
    # cities = Cities.objects.all() #mind the s in objects
    # data = []
    # for city in cities:
    #     ###make the call and get back the request in json format
    #     r = requests.get(url.format(city)).json()
    #     #print(r.text)

    #     ###save the data to pass to the template as context
    #     weathers = {
    #         'city': city.name,  #it should be like this as you are getting the city name from the database, which was returned to you as objects
    #         'temperature': r['main']['temp'], #the main is a dict
    #         'description': r['weather'][0]['description'],  #weather is a list, so it need an int index first
    #         'icon': r['weather'][0]['icon'], 
    #     }
    #     #print(weathers)

    #     data.append(weathers)
    # data = data[-1]  #cuz I don't want to see a list of cities all the time
    context = {'weathers': data, 'form': form, 'message': msg}
    return render(request, 'index.html', context)
