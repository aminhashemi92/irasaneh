from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('company', company, name='company'),
    path('changepass', changepass, name='changepass'),
    path('employee', employee, name='employee'),
    path('myofflineresaneh', myofflineresaneh, name='myofflineresaneh'),
    path('mydigitalresaneh', mydigitalresaneh, name='mydigitalresaneh'),

    path('vod', vodDashboard, name='vodDashboard'),
    path('vodResanehs', vodResanehs, name='vodResanehs'),
    path('vodResanehAdd', vodResanehAdd, name='vodResanehAdd'),
    path('vodResanehDelete/<int:pk>', vodResanehDelete, name="vodResanehDelete"),
    path('vodResanehUpdate/<slug:slug>', vodResanehUpdate, name="vodResanehUpdate"),
    path('vodVideos', vodVideos, name='vodVideos'),
    path('vodVideoAdd', vodVideoAdd, name='vodVideoAdd'),
    path('vodVideoUpdate/<int:pk>', vodVideoUpdate, name="vodVideoUpdate"),
    path('vodVideoDelete/<int:pk>', vodVideoDelete, name="vodVideoDelete"),
    path('vodBoxes', vodBoxes, name='vodBoxes'),
    path('vodBoxAdd', vodBoxAdd, name='vodBoxAdd'),
    path('vodBoxUpdate/<int:pk>', vodBoxUpdate, name="vodBoxUpdate"),
    path('vodBoxDelete/<int:pk>', vodBoxDelete, name="vodBoxDelete"),
    path('vodEvents', vodEvents, name='vodEvents'),
    path('vodEventAdd', vodEventAdd, name='vodEventAdd'),
    path('vodEventUpdate/<int:pk>', vodEventUpdate, name="vodEventUpdate"),
    path('vodEventDelete/<int:pk>', vodEventDelete, name="vodEventDelete"),

    path('charts', charts, name="charts"),
    path('lastlog', lastlog, name="lastlog"),
    path('chartjs', chartjs, name="chartjs"),
    path('flot', flot, name="flot"),
    path('inline', inline, name="inline"),


    path('Videos', Videos, name='Videos'),
    path('VideoAdd', VideoAdd, name='VideoAdd'),
    path('VideoUpdate/<int:pk>', VideoUpdate, name="VideoUpdate"),
    path('VideoDelete/<int:pk>', VideoDelete, name="VideoDelete"),

    path('ajax/load-counterChart/', load_counterChart, name='ajax_load_counterChart'),


]
