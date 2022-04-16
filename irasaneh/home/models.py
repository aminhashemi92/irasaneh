from django.db import models

# Create your models here.
class ContactUs(models.Model):
    ROLE_CHOICES =(
        ('k', 'رسانه‌خواه'),
        ('b', 'رسانه‌دار'),
    )

    firstname = models.CharField(max_length=200, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=200, null=True, verbose_name="نام‌خانوادگی")
    title = models.CharField(max_length=200, null=True, verbose_name="عنوان پیام")
    description = models.TextField(verbose_name="توضیحات",blank=True)
    role = models.CharField(max_length=1, null=True, choices = ROLE_CHOICES, verbose_name="نقش")
    mphone = models.CharField(max_length=200, null=True, verbose_name="تلفن")
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی‌پی', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "فرم ارتباط با ما"
        verbose_name_plural = "فرم‌های ارتباط با ما"

    def __str__(self):
        return self.title
