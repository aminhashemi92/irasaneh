from django.urls import path
from .views import *

app_name = "cities"
urlpatterns = [
    path('ajax/load-states/', load_states, name='ajax_load_states'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('ajax/load-zones/', load_zones, name='ajax_load_zones'),
]
