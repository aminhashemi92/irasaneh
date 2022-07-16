from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from resaneh.models import Resaneh
from django.core.validators import FileExtensionValidator
from account.models import Company
# Create your models here.

class AdVideoType(models.Model):
    title = models.CharField(max_length=200, verbose_name="نوع ویدیو", blank=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "نوع ویدیو"
        verbose_name_plural = "انواع ویدیو"

    def __str__(self):
        return str(self.title)


class AdVideo(models.Model):
    CONDITION_CHOICES = (
        ('p', 'پیش‌نویس'),
        ('d', 'در انتظار بررسی'),
        ('y', 'تایید شده'),
        ('n', 'رد شده'),
    )
    name = models.CharField(max_length=200, verbose_name="نام ویدیو", blank=True)
    type = models.ForeignKey(AdVideoType, verbose_name="نوع", blank=True, null=True, on_delete=models.SET_NULL,related_name="advideo")
    owner =  models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name="advideo", verbose_name="ایجاد کننده")
    company =  models.ForeignKey(Company, null=True, on_delete=models.SET_NULL, related_name="advideo", verbose_name="صاحب ویدیو", blank=True)#شرکت صاحب ویدیو
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    video = models.FileField(upload_to='advideos',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','jpg'])], verbose_name="ویدیو", blank=True)

    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES,default='p',verbose_name="وضعیت انتشار", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ویدیو"
        verbose_name_plural = "ویدیوها"

    def __str__(self):
        return str(self.name)

    def mstatus(self):
        if self.status == True:
            a = "<img src='/static/admin/img/icon-yes.svg' alt='True'>"
        else:
            a = "<img src='/static/admin/img/icon-no.svg' alt='False'>"
        return format_html(a)
        # return format_html("<img style='width:55px;' src='{}'".format(self.thumbnail.url))


class AdBox(models.Model):
    owner =  models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name="adbox", verbose_name="ایجاد کننده", blank=True)
    name = models.CharField(max_length=200, verbose_name="نام باکس آگهی", blank=True)
    numberOfVideos = models.PositiveIntegerField(verbose_name="تعداد ویدیوها", blank=True)
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    order =  models.CharField(max_length=200, verbose_name="ترتیب نمایش فیلم‌ها", blank=True,help_text='اعداد را به انگلیسی وارد کنید و با - فاصله دهید.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    videos = models.ManyToManyField(AdVideo, verbose_name="ویدیوها", related_name="adbox")

    videos_list = models.CharField(max_length=200, verbose_name="ویدیو‌های مرتب شده", blank=True)

    class Meta:
        verbose_name = "باکس"
        verbose_name_plural = "باکس‌ها"

    # def save_related(self, request, form, formsets, change):
    #     super(AdBox, self).save_related(request, form, formsets, change)
    #     videos = self.videosvideo_id_list = list(videos.values_list('id', flat=True))
    #     orders = self.order
    #     orders_list = map(int, orders.split('-'))
    #     z = [x for _,x in sorted(zip(orders_list,video_id_list))]
    #     video_play_list = ','.join(map(str, z))
    #     # print(orders_list)
    #     # A = self.save()
    #     self.videos_list = video_play_list
    #     super(AdBox, self).save_related(request, form, formsets, change)



    def __str__(self):
        return str(self.name)

    # def save(self, *args, **kwargs):
    #     super(AdBox, self).save(*args, **kwargs)
    #     videos = self.videos
    #     video_id_list = list(videos.values_list('id', flat=True))
    #     orders = self.order
    #     orders_list = map(int, orders.split('-'))
    #     z = [x for _,x in sorted(zip(orders_list,video_id_list))]
    #     video_play_list = ','.join(map(str, z))
    #     # print(orders_list)
    #     # A = self.save()
    #     self.videos_list = video_play_list
    #     super(AdBox, self).save(*args, **kwargs)

    def mstatus(self):
        if self.status == True:
            a = "<img src='/static/admin/img/icon-yes.svg' alt='True'>"
        else:
            a = "<img src='/static/admin/img/icon-no.svg' alt='False'>"
        return format_html(a)




class AdEvent(models.Model):
    owner =  models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name="adevent", verbose_name="ایجاد کننده", blank=True)
    name = models.CharField(max_length=200, verbose_name="نام", blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models. BooleanField(default=True, verbose_name="نمایش داده شود؟")
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    media = models.ForeignKey(AdBox, null=True, on_delete=models.SET_NULL, related_name="adevent", verbose_name="باکس", blank=True)
    resaneh = models.ManyToManyField(Resaneh,related_name="adevent", verbose_name="رسانه", blank=True)
    startTime = models.TimeField(default=timezone.now, verbose_name="ساعت شروع")
    endTime = models.TimeField(default=timezone.now, verbose_name="ساعت پایان")
    startDate = models.DateTimeField(default=timezone.now, verbose_name="زمان شروع")
    endDate = models.DateTimeField(default=timezone.now, verbose_name="زمان پایان")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"

    def __str__(self):
        return str(self.name)

    def jstartDate(self):
        return jalali_converter(self.startDate).split(',')[0]
    jstartDate.short_description = "تاریخ شروع"

    def jendDate(self):
        return jalali_converter(self.endDate).split(',')[0]
    jendDate.short_description = "تاریخ پایان"

    def resaneh_active(self):
        return self.resaneh.filter(status='p')

    def mstatus(self):
        if self.status == True:
            a = "<img src='/static/admin/img/icon-yes.svg' alt='True'>"
        else:
            a = "<img src='/static/admin/img/icon-no.svg' alt='False'>"
        return format_html(a)


class AdConnectionLog(models.Model):
    resaneh = models.ForeignKey(Resaneh,verbose_name="رسانه",blank=True,on_delete=models.SET_NULL, related_name="adconnectionlog", null=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    created = models.DateTimeField(default=timezone.now,verbose_name="زمان ایجاد", blank=True)


class AdApplicationLog(models.Model):
    resaneh = models.ForeignKey(Resaneh,verbose_name="رسانه",blank=True,on_delete=models.SET_NULL, related_name="adapplicationlog", null=True)
    name = models.CharField(max_length=200, verbose_name="نام", blank=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    created = models.DateTimeField(default=timezone.now,verbose_name="زمان ایجاد", blank=True)


class AdVideoLog(models.Model):
    resaneh = models.ForeignKey(Resaneh,verbose_name="رسانه",blank=True,on_delete=models.SET_NULL, related_name="advideolog", null=True)
    video = models.ForeignKey(AdVideo,verbose_name="ویدیو",blank=True,on_delete=models.SET_NULL, related_name="advideolog", null=True)
    box = models.ForeignKey(AdBox,verbose_name="باکس",blank=True,on_delete=models.SET_NULL, related_name="advideolog", null=True)
    name = models.CharField(max_length=200, verbose_name="نام", blank=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    created = models.DateTimeField(default=timezone.now,verbose_name="زمان ایجاد", blank=True)


class AdVideoCounterLog(models.Model):
    resaneh = models.ForeignKey(Resaneh,verbose_name="رسانه",blank=True,on_delete=models.SET_NULL, related_name="advideocounterlog", null=True)
    video = models.ForeignKey(AdVideo,verbose_name="ویدیو",blank=True,on_delete=models.SET_NULL, related_name="advideocounterlog", null=True)
    box = models.ForeignKey(AdBox,verbose_name="باکس",blank=True,on_delete=models.SET_NULL, related_name="advideocounterlog", null=True)
    detail = models.TextField(verbose_name="جزییات بیشتر", blank=True)
    created = models.DateTimeField(default=timezone.now,verbose_name="زمان ایجاد", blank=True)
