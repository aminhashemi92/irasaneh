from django.db import models
from account.models import CustomUser
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from account.models import Company
from location_field.models.plain import PlainLocationField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from hitcount.models import HitCountMixin, HitCount
from star_ratings.models import Rating
# from comment.models import Comment

# Managers
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
# class ImageResanehManager(models.Manager):
#     def coverimage(self):
#         return self.resanehimage.first()

# Create your models here.
class Industry(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان صنعت")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس صنعت")
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "صنعت"
        verbose_name_plural = "صنایع"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title



class Tag(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان تگ")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس تگ")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ‌ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    detail = models.TextField(verbose_name="توضیحات", blank=True)
    pcode = models.CharField(max_length=200, verbose_name="کد جایگاه", blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "جایگاه"
        verbose_name_plural = "جایگاه‌ها"
        ordering = ['position',]

    def __str__(self):
        return self.title






# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)
    thumbnail = models.ImageField(upload_to="categoryimages", verbose_name="تصویر", null=True, blank=True)
    class Meta:
        verbose_name = "نوع رسانه"
        verbose_name_plural = "انواع رسانه"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class ShowType(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)

    class Meta:
        verbose_name = "نوع نمایش"
        verbose_name_plural = "انواع نمایش"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title


class StructureType(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)

    class Meta:
        verbose_name = "نوع سازه"
        verbose_name_plural = "انواع سازه"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title



class Resaneh(models.Model):
    STATUS_CHOICES = (
        ('p', 'فعال'),
        ('d', 'غیرفعال'),
    )


    creator = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="ایجاد کننده", blank=True)
    company = models.ForeignKey(Company , null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="رسانه‌دار", blank=True)
    place = models.ForeignKey(Place , null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="گروه رسانه", blank=True)

    name = models.CharField(max_length=200, verbose_name="نام رسانه", blank=True)
    owner = models.CharField(max_length=200, verbose_name="مالک رسانه", blank=True)
    dimensions = models.CharField(max_length=200, verbose_name="ابعاد", blank=True)
    area =  models.CharField(max_length=200, verbose_name="مساحت", blank=True)
    areadetail = models.CharField(max_length=200, verbose_name="جزییات مساحت", blank=True)
    address = models.CharField(max_length=200, verbose_name="آدرس", blank=True)
    location = PlainLocationField(default='35.69977923732504,411.33733749345987',zoom=7, blank=True)

    nvisit = models.CharField(max_length=200, verbose_name="برآورد بازدید روزانه", blank=True)

    price = models.PositiveIntegerField(verbose_name="قیمت", blank=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    point = models.TextField(verbose_name="امتیازات", blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    slug =  models.SlugField(max_length=100, unique=True, verbose_name="آدرس صفحه")
    code = models.CharField(max_length=200, verbose_name="کد شناسایی", blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    industry = models.ManyToManyField(Industry, verbose_name="صنعت", related_name="resaneh")
    tag = models.ManyToManyField(Tag, verbose_name="تگ", related_name="resaneh")
    category = models.ManyToManyField(Category, verbose_name="نوع رسانه", blank=True, related_name="resaneh")
    showtype = models.ManyToManyField(ShowType, verbose_name="نوع نمایش", blank=True, related_name="resaneh")
    structuretype = models.ForeignKey(StructureType, verbose_name="نوع سازه", blank=True, null=True, on_delete=models.SET_NULL, related_name="resaneh")

    comments = GenericRelation(Comment)
    viewed = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    ratings = GenericRelation(Rating, related_query_name='resaneh')


    class Meta:
        verbose_name = "رسانه"
        verbose_name_plural = "رسانه‌ها"

    def __str__(self):
        return self.name

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان ایجاد"

    def industry_published(self):
        return self.industry.filter(status=True)

    def tag_published(self):
        return self.tag.filter(status=True)

    def category_published(self):
        return self.category.filter(status=True)

    def showtype_published(self):
        return self.showtype.filter(status=True)

    # objects = ImageResanehManager()


class ResanehImage(models.Model):
    resaneh = models.ForeignKey(Resaneh, default=None, related_name="resanehimage", verbose_name="رسانه", on_delete=models.CASCADE, blank=True)
    image = models.FileField(upload_to='resanehimages', verbose_name="عکس")

    class Meta:
        verbose_name = "عکس‌های رسانه"
        verbose_name_plural = "عکس‌های رسانه‌ها"

    def __str__(self):
        return self.resaneh.name

    def image_tag(self):
        return format_html("<img style='width:55px;' src='{}'>".format(self.image.url))
    image_tag.short_description = "تصویر"
