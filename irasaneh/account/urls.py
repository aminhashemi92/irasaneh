from django.urls import path, include
from .views import *

app_name = "account"
urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('phoneOtp', phoneOtp, name='phoneOtp'),
    path('codeOtp', codeOtp, name='codeOtp'),
    path('logout_page',logoutUser,name="logout_page"),

]
