from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    path('', blog, name='blog'),
    path('page/<int:page>', blog, name='blog'),
    path('<slug:slug>', single, name="single") ,
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/page/<int:page>', category, name='category'),
    path('search/', search, name='search'),
    path('search/page/<int:page>', search, name='search'),
]
