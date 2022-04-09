from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('employee', employee, name='employee'),
    path('myresaneh', myresaneh, name='myresaneh'),
]
