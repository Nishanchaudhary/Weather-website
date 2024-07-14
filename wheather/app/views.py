from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='kathmandu'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0cf7889ff494aaa5a23d6d547c40caef"
    params={'units':'metric'}
    try:
        data = requests.get(url, params).json() #json format to python dictionary
        temp = data['main']['temp']
        desc=data['weather'][0]['description']
        wind=data['wind']['speed']
        icon=data['weather'][0]['icon']
        humidity=data['main']['humidity']
        return render(request,'index.html',{'temp':temp,'city':city, 'desc':desc,'wind':wind,'icon':icon,'humidity':humidity,})
    except:
        data = requests.get(url, params).json() #json format to python dictionary
        temp =0
        desc="no such data"
        wind=5
        icon="no data found"
        humidity=5
        messages.error(request,'no such city name !!!')
        return render(request,'index.html',{'temp':temp,'city':city, 'desc':desc,'wind':wind,'icon':icon,'humidity':humidity,})
    