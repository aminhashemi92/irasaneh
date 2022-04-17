from django.contrib import admin
from .models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Country,CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    list_filter = (['country',])
    search_fields = ('name','country')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','state')
    list_filter = (['state',])
    search_fields = ('name','state')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(City,CityAdmin)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name','city')
    list_filter = (['city',])
    search_fields = ('name','city')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Zone,ZoneAdmin)
