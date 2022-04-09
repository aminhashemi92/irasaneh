from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('', homepage, name='homepage'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('faq', faq, name='faq'),
]
