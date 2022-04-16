from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'title', 'role','ip_address')
    list_filter = ('role',)
    ordering = ['date_created', ]
    search_fields = ('firstname','lastname','title','description')
admin.site.register(ContactUs, ContactUsAdmin)
