from django.urls import path
from .views import *

app_name = "resaneh"
urlpatterns = [
    path('', resaneh, name='resaneh'),
    path('page/<int:page>', resaneh, name='resaneh'),
    path('<slug:slug>', resaneh, name='resaneh'),
    path('<slug:slug>/page/<int:page>', resaneh, name='resaneh'),
    path('details/<slug:slug>', details, name='details'),
    # path('category/<slug:slug>', category, name='category'),
    # path('category/<slug:slug>/page/<int:page>', category, name='category'),
    path('search/', search, name='search'),
    path('search/page/<int:page>', search, name='search'),
]
