from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('employee', employee, name='employee'),
    path('myresaneh', myresaneh, name='myresaneh'),

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

]
