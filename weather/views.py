import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=5b73bfe661d8e16857ff742297a0beaf'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        #return HttpResponseRedirect('localhost')
    form = CityForm()

    city = City.objects.order_by('-id')[0]
    print(city)
    r = requests.get(url.format(city)).json()
    city_detail = {
            'city': r['name'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'temperature': r['main']['temp']
    }

    print(city_detail)

    context = {'city_detail': city_detail, 'form': form}
    return render(request, 'weather/index.html', context)


def index1(request):
    return render(request, 'weather/index1.html')


def index2(request):
    return render(request, 'weather/index2.html')
