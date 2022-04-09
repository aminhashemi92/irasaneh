from django.contrib import admin
from .models import Article, Category, IPAddress
from django_summernote.admin import SummernoteModelAdmin



# actions
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "انتشار خبرهای انتخاب شده"

def make_draf(modeladmin, request, queryset):
    queryset.update(status='d')
make_draf.short_description = "پیش نویس شدن خبرهای انتخاب شده"

def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
make_active.short_description = "فعال شدن دسته‌بندی‌های انتخاب شده"

def make_diactive(modeladmin, request, queryset):
    queryset.update(status=False)
make_diactive.short_description = "غیرفعال شدن دسته‌بندی‌های انتخاب شده"


# class ArticleAdmin(admin.ModelAdmin):
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['parent','status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(Category,CategoryAdmin)




class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title','thumbnail_tag', 'slug', 'author','jpublish', 'status', 'category_to_str',)
    list_filter = ('publish', 'status',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draf]

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = "دسته‌بندی‌ها"


admin.site.register(Article,ArticleAdmin)


admin.site.register(IPAddress)
