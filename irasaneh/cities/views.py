from django.shortcuts import render
from .models import *

# Create your views here.
def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'cities/state_dropdown_list_options.html', {'states': states})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'cities/city_dropdown_list_options.html', {'cities': cities})


def load_zones(request):
    city_id = request.GET.get('city')
    zones = Zone.objects.filter(city_id=city_id).order_by('id')
    return render(request, 'cities/zone_dropdown_list_options.html', {'zones': zones})
