from django.shortcuts import render
import json
import urllib.request

def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        key = 'APIKEY'
        url = urllib.request.urlopen('https://api.weatherbit.io/v2.0/current?city='+city+'&key='+key).read()
        j_response = json.loads(url)
        temperature = j_response['data'][0]['temp']
        data = {"Temperature":str(temperature),
                "City":city,
        }
        print(data)
    else:
        data = {}

    return render (request,'home.html',data)
