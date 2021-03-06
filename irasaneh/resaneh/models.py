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
from cities.models import *


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

    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name="place", verbose_name="کشور", blank=True)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL, related_name="place", verbose_name="استان", blank=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, related_name="place", verbose_name="شهر", blank=True)
    zone = models.ForeignKey(Zone, null=True, on_delete=models.SET_NULL, related_name="place", verbose_name="منطقه", blank=True)

    address = models.CharField(max_length=200, verbose_name="آدرس", blank=True)

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


class IncomeTithe(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)

    class Meta:
        verbose_name = "دهک درآمدی"
        verbose_name_plural = "دهک‌های درآمدی"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title


class Ages(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)

    class Meta:
        verbose_name = "رده‌ی سنی"
        verbose_name_plural = "رده‌های سنی"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title


class Gender(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL ,related_name='children' ,verbose_name='زیرشاخه')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن", default=1)

    class Meta:
        verbose_name = "جنسیت"
        verbose_name_plural = "جنسیت‌ها"
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

    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="کشور", blank=True)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="استان", blank=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="شهر", blank=True)
    zone = models.ForeignKey(Zone, null=True, on_delete=models.SET_NULL, related_name="resaneh", verbose_name="منطقه", blank=True)


    address = models.CharField(max_length=200, verbose_name="آدرس", blank=True)
    location = PlainLocationField(default='35.69977923732504,411.33733749345987',zoom=7, blank=True)

    nvisit = models.CharField(max_length=200, verbose_name="برآورد بازدید روزانه", blank=True)

    price = models.PositiveIntegerField(verbose_name="قیمت", blank=True, default=0)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    point = models.TextField(verbose_name="امتیازات", blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    # slug =  AutoSlugField(populate_from=['name',])
    slug =  models.SlugField(max_length=100, unique=True, verbose_name="آدرس صفحه")
    code = models.CharField(max_length=200, verbose_name="کد شناسایی", blank=True)
    connectionID = models.CharField(max_length=200, verbose_name="کد ارتباطی", blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    industry = models.ManyToManyField(Industry, verbose_name="صنعت", related_name="resaneh")
    tag = models.ManyToManyField(Tag, verbose_name="تگ", related_name="resaneh")
    category = models.ManyToManyField(Category, verbose_name="نوع رسانه", blank=True, related_name="resaneh")
    showtype = models.ManyToManyField(ShowType, verbose_name="نوع نمایش", blank=True, related_name="resaneh")
    structuretype = models.ForeignKey(StructureType, verbose_name="نوع سازه", blank=True, null=True, on_delete=models.SET_NULL, related_name="resaneh")
    gender = models.ManyToManyField(Gender, verbose_name="جنسیت", blank=True, related_name="resaneh")
    incometithe = models.ManyToManyField(IncomeTithe, verbose_name="دهک درآمدی", blank=True, related_name="resaneh")
    ages = models.ManyToManyField(Ages, verbose_name="رده‌ی سنی", blank=True, related_name="resaneh")

    comments = GenericRelation(Comment)
    viewed = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    ratings = GenericRelation(Rating, related_query_name='resaneh')


    is_digital = models.BooleanField(default=False, verbose_name="رسانه‌ی دیجیتال")
    tvModel = models.CharField(max_length=200, verbose_name="مدل تلویزیون", blank=True)
    tvSize = models.CharField(max_length=200, verbose_name="ابعاد تلویزیون", blank=True)
    is_Androidbox = models.BooleanField(default=False, verbose_name="سیستم‌عامل اندروید")
    androidVersion = models.CharField(max_length=200, verbose_name="ورژن اندروید", blank=True)
    operatorNumber = models.CharField(max_length=200, blank=True, verbose_name="تلفن اپراتور")


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

    def mis_Androidbox(self):
        if self.is_Androidbox == True:
            a = "<img src='/static/admin/img/icon-yes.svg' alt='True'>"
        else:
            a = "<img src='/static/admin/img/icon-no.svg' alt='False'>"
        return format_html(a)

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


class Offer(models.Model):
    resaneh = models.ForeignKey(Resaneh, default=None, related_name="resanehoffer", verbose_name="رسانه", on_delete=models.CASCADE, blank=True)
    start = models.DateTimeField(default=timezone.now, verbose_name="زمان شروع")
    end = models.DateTimeField(default=timezone.now, verbose_name="زمان پایان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    status = models. BooleanField(default=False, verbose_name="فعال")
    class Meta:
        verbose_name = "پیشنهاد ویژه"
        verbose_name_plural = "پیشنهاد‌های ویژه"

    def __str__(self):
        return self.resaneh.name

    def is_active(self):
        if self.end > timezone.now() and self.status==True:
            return True
        else:
            return False

    is_active.boolean = True
    is_active.short_description = "نمایش داده شود؟"

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "زمان ایجاد"

    def jstart(self):
        return jalali_converter(self.start)
    jstart.short_description = "زمان شروع"

    def jend(self):
        return jalali_converter(self.end)
    jend.short_description = "زمان پایان"
