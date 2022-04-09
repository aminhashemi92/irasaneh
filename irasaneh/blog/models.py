from django.db import models
from account.models import CustomUser
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating



# Managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)



# Create your models here.
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی‌پی')



class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده'),
    )
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="تیتر خبر")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    minidescription = models.CharField(max_length=500, verbose_name="خلاصه")
    description = models.TextField(verbose_name="متن")
    thumbnail = models.ImageField(upload_to="blogimages", verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, blank=True, related_name='hits', verbose_name='بازدیدها')
    ratings = GenericRelation(Rating, related_query_name='articles')
    # rate = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="امتیاز", default=0.00)

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "خبرها"

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img style='width:55px;' src='{}'".format(self.thumbnail.url))
    thumbnail_tag.short_description = "تصویر"


# from django.db import models
# from django.utils import timezone
#
#
# # Create your models here.
# class Article(models.Model):
#     STATUS_CHOICES = (
#         ('d', 'draft'),
#         ('p', 'publish'),
#     )
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=100, unique=True)
#     description = models.TextField()
#     thumbnail = models.ImageField(upload_to="blogimages")
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES)
#
#     def __str__(self):
#         return self.title
