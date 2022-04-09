from django.urls import path, include
from .views import *

app_name = "account"
urlpatterns = [
    path('login_register', login_register, name='login_register'),
    path('logout_page',logoutUser,name="logout_page"),

]
