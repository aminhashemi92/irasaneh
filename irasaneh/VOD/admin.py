from django.contrib import admin
from .models import *


# actions
def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
make_active.short_description = "فعال شدن دسته‌بندی‌های انتخاب شده"

def make_diactive(modeladmin, request, queryset):
    queryset.update(status=False)
make_diactive.short_description = "غیرفعال شدن دسته‌بندی‌های انتخاب شده"


# Register your models here.
class AdVideoTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    list_filter = ([ 'status', ])
    search_fields = ('title', 'detail')
    actions = [make_active, make_diactive]

admin.site.register(AdVideoType,AdVideoTypeAdmin)


class AdVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner', 'status', 'video')
    list_filter = ([ 'owner', 'type', 'status'])
    search_fields = ('name', 'owner')
    actions = [make_active, make_diactive]

admin.site.register(AdVideo,AdVideoAdmin)

class AdBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'numberOfVideos','status')
    list_filter = (['status'])
    search_fields = ('name',)
    actions = [make_active, make_diactive]

admin.site.register(AdBox,AdBoxAdmin)

class AdEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'jstartDate','jendDate', 'resaneh_to_str','status')
    list_filter = (['status'])
    search_fields = ('name', 'detail')
    prepopulated_fields = {'slug':('name',)}
    actions = [make_active, make_diactive]

    def resaneh_to_str(self, obj):
        return "، ".join([resaneh.name for resaneh in obj.resaneh_active()])
    resaneh_to_str.short_description ="رسانه‌ها"

admin.site.register(AdEvent,AdEventAdmin)


class AdConnectionLogAdmin(admin.ModelAdmin):
    list_display = ('resaneh', 'created',)
    list_filter = ([ 'resaneh', ])
    search_fields = ('resaneh', 'detail')

admin.site.register(AdConnectionLog,AdConnectionLogAdmin)


class AdApplicationLogAdmin(admin.ModelAdmin):
    list_display = ('resaneh', 'name', 'created',)
    list_filter = ([ 'resaneh', 'name',])
    search_fields = ('resaneh', 'name','detail')

admin.site.register(AdApplicationLog,AdApplicationLogAdmin)


class AdVideoLogAdmin(admin.ModelAdmin):
    list_display = ('resaneh', 'video', 'box', 'name', 'created')
    list_filter = ([ 'resaneh', 'video', 'box', 'name', ])
    search_fields = ('resaneh', 'video', 'box', 'name','detail')

admin.site.register(AdVideoLog,AdVideoLogAdmin)


class AdVideoCounterLogAdmin(admin.ModelAdmin):
    list_display = ('resaneh', 'video', 'box', 'created')
    list_filter = ([ 'resaneh', 'video', 'box', ])
    search_fields = ('resaneh', 'video', 'box', 'detail')

admin.site.register(AdVideoCounterLog,AdVideoCounterLogAdmin)
