from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponse
from django.shortcuts import render
from geopy import distance as d
from geopy.geocoders import Nominatim

from .forms import DestinationFieldForm



def request_handler_calculate(request):
    if request.method == 'POST':

        form = DestinationFieldForm(request.POST or None)
        

        geolocator = Nominatim(user_agent="calculate_app")
        ip = "103.139.234.0" #Dhaka Bangladesh
        country,city,latitude,longitude = get_info(ip)
        origin = (latitude,longitude)

        # print(country,geolocator.geocode(city),latitude,longitude)
        # print(city['city'])

        if form.is_valid():
            
            location = city['city']
            destination_data_fieldform = form.cleaned_data.get('destination')
            destination_details = geolocator.geocode(destination_data_fieldform)
            destination_co_ordinates = (destination_details.latitude,destination_details.longitude)
            distance = d.distance(origin, destination_co_ordinates).km

        return render(request, 'main_app_template.html',{'data': [str(round(distance,2)),city['city'],destination_data_fieldform]})


    else:

        return render(request, 'main_app_template.html',{'hi':'hi'})


def get_info(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    latitude,longitude = g.lat_lon(ip)
    return country,city,latitude,longitude
