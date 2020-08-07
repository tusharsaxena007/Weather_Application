from django.shortcuts import render, HttpResponse, redirect,reverse
import requests
from .models import city
from .forms import cityform

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=daaf2d5837d08f668710cdc4bddd56a3'


def add(request):
    if request.POST:
        form = cityform(request.POST)

        if form.is_valid():
            new_city_name = form.cleaned_data['name']
            try:
               c = city.objects.get(name = form.cleaned_data['name'].lower())
               return redirect(reverse('index'))
            except:
               city.objects.create(name = new_city_name.lower())
               return redirect(reverse('index'))

        return HttpResponse("FORM INVALID")

    else:
       return redirect(reverse('index'))

def homepage(request):
    if request.method =='GET':
        form = cityform
        c = city.objects.all()
        for i in c:
            data = requests.get(url.format(i.name)).json()
            i.temperature = data['main']['temp']-273.
            i.image = data['weather'][0]['icon']
            i.condition = data['weather'][0]['description']


    return render(request,'weather/homepage.html',{'objects':c,'form':form})



def delete(request,name):
    delete_city = city.objects.get(name=name)
    delete_city.delete()
    return redirect(reverse('index'))

