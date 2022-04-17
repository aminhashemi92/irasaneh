from django.contrib import admin
from .models import *




# actions
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "انتشار موارد انتخاب شده"

def make_draf(modeladmin, request, queryset):
    queryset.update(status='d')
make_draf.short_description = "پیش نویس شدن موارد انتخاب شده"

def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
make_active.short_description = "فعال شدن دسته‌بندی‌های انتخاب شده"

def make_diactive(modeladmin, request, queryset):
    queryset.update(status=False)
make_diactive.short_description = "غیرفعال شدن دسته‌بندی‌های انتخاب شده"


# class ArticleAdmin(admin.ModelAdmin):
# class IndustryAdmin(admin.ModelAdmin):
#     list_display = ('position', 'title', 'slug', 'status')
#     list_filter = (['status'])
#     search_fields = ('title', 'slug')
#     prepopulated_fields = {'slug':('title',)}
#     actions = [make_active, make_diactive]
#
# admin.site.register(Industry,IndustryAdmin)
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('position', 'title', 'slug', 'status')
#     list_filter = (['status'])
#     search_fields = ('title', 'slug')
#     prepopulated_fields = {'slug':('title',)}
#     actions = [make_active, make_diactive]
#
# admin.site.register(Tag,TagAdmin)
#
#
#
#
# class ResanehAdmin(admin.ModelAdmin):
#     list_display = ('name','company', 'category', 'showtype', 'industry_to_str', 'tag_to_str','status',)
#     list_filter = ('category', 'showtype', 'status', 'company')
#     search_fields = ('name', 'description', 'company')
#     prepopulated_fields = {'slug':('name',)}
#     ordering = ['status', 'publish']
#     actions = [make_published, make_draf]
#
#     def industry_to_str(self, obj):
#         return "، ".join([category.title for category in obj.industry_published()])
#
#     industry_to_str.short_description ="صنایع"
#
#     def tag_to_str(self, obj):
#         return "، ".join([tag.title for tag in obj.tag_published()])
#
#     tag_to_str.short_description ="تگ‌ها"
#
# admin.site.register(Resaneh,ResanehAdmin)


# class ResanehImageAdmin(admin.ModelAdmin):
#     list_display = ('resaneh','image_tag',)
#     list_filter = ('resaneh',)
#     search_fields = ('resaneh',)

# admin.site.register(ResanehImage,ResanehImageAdmin)


class ResanehImageAdmin(admin.StackedInline):
    model = ResanehImage
    list_display = ('resaneh','image_tag',)
    list_filter = ('resaneh',)
    search_fields = ('resaneh',)


# class ArticleAdmin(admin.ModelAdmin):
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = ([ 'parent', 'status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(Industry,IndustryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['parent','status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(Tag,TagAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status', 'title'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(Place,PlaceAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = ([ 'parent', 'status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(Category,CategoryAdmin)



class ShowTypeAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = ([ 'parent', 'status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(ShowType,ShowTypeAdmin)


class StructureTypeAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = ([ 'parent', 'status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_active, make_diactive]

admin.site.register(StructureType,StructureTypeAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('resaneh', 'jstart', 'jend', 'jcreated', 'status', 'is_active')
    list_filter = (['status',])
    search_fields = ('resaneh', )
    actions = [make_active, make_diactive]

admin.site.register(Offer,OfferAdmin)


@admin.register(Resaneh)
class ResanehAdmin(admin.ModelAdmin):
    inlines = [ResanehImageAdmin]
    list_display = ('name','company','place','category_to_str','showtype_to_str','status',)
    list_filter = ( 'status', 'company','place')
    search_fields = ('name', 'detail')
    prepopulated_fields = {'slug':('name',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draf]

    class Meta:
       model = Resaneh

    def industry_to_str(self, obj):
        return "، ".join([category.title for category in obj.industry_published()])
    industry_to_str.short_description ="صنایع"

    def tag_to_str(self, obj):
        return "، ".join([tag.title for tag in obj.tag_published()])
    tag_to_str.short_description ="تگ‌ها"

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])
    category_to_str.short_description ="دسته‌بندی‌ها"

    def showtype_to_str(self, obj):
        return "، ".join([showtype.title for showtype in obj.showtype_published()])
    showtype_to_str.short_description ="نمایش‌ها"


@admin.register(ResanehImage)
class ResanehImageAdmin(admin.ModelAdmin):
    list_display = ('resaneh','image_tag',)
    list_filter = ('resaneh',)
    search_fields = ('resaneh',)


# admin.site.register(Resaneh,ResanehAdmin)

# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
#
#     class Meta:
#        model = Post
#
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass
