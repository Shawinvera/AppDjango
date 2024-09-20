import urllib.request
import json
from django.shortcuts import render

def index(request):
    data = {}
    
    if request.method == 'POST':
        city = request.POST['city']
        # Make sure to use your actual API key here
        url ='http://api-openweathermap.org/data/2.5/weather?q=' + city + '&appid=d4c02beb0bc29b804de34d5387a5a7f7'  # Added units=metric for °C
        
        try:
            with urllib.request.urlopen(url) as response:
                source = response.read()
                list_of_data = json.loads(source)

                data = {
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
                    "temp": f"{list_of_data['main']['temp']} °C",
                    "pressure": str(list_of_data['main']['pressure']),
                    "humidity": str(list_of_data['main']['humidity']),
                    "main": str(list_of_data['weather'][0]['main']),
                    "description": str(list_of_data['weather'][0]['description']),
                    "icon": list_of_data['weather'][0]['icon'],
                }
                print(data)
        except Exception as e:
            print(f"Error fetching data: {e}")
            data['error'] = "Could not retrieve data. Please check the city name."

    return render(request, 'base.html', {'data': data})  # Correct the path to the template
