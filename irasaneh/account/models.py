from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse
from extensions.utils import jalali_converter
from django.core.validators import RegexValidator

# Manager
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

# Model
class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, validators=[RegexValidator( regex=r'^[0]{1}[9]{1}[0-9]{9}', message='مقدار وارد شده صحیح نمی‌باشد',)], unique=True, verbose_name='Phone Number', blank=False, help_text='Enter 10 digits phone number')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


# Model
class Company(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="نام",  blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, verbose_name="تاریخ ایجاد",  blank=True)
    logo = models.ImageField(upload_to="companyimages", null=True, verbose_name="لوگو", default="profileimages/profi.png")
    sphone = models.CharField(max_length=200, null=True, verbose_name="تلفن ثابت", blank=True)
    mphone = models.CharField(max_length=200, null=True, verbose_name="تلفن همراه", blank=True)

    class Meta:
        verbose_name = "شرکت"
        verbose_name_plural = "شرکت‌ها"

    def __str__(self):
        return str(self.name)


    def logo_tag(self):
        return format_html("<img style='width:55px;' src='{}'>".format(self.logo.url))
    logo_tag.short_description = "تصویر"


# Model
class Profile(models.Model):
    ROLE_CHOICES =(
        ('k', 'رسانه‌خواه'),
        ('b', 'رسانه‌دار و رسانه‌خواه'),
    )
    POSITION_CHOICES =(
        ('c', 'کارمند'),
        ('m', 'مدیر'),
    )

    user = models.OneToOneField(CustomUser, null = True, on_delete = models.CASCADE, verbose_name="کاربر", related_name="profile")
    firstname = models.CharField(max_length=200, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=200, null=True, verbose_name="نام‌خانوادگی")
    company = models.ForeignKey(Company, default=None, null=True, related_name="profile", verbose_name="شرکت", on_delete=models.CASCADE, blank=True)
    role = models.CharField(max_length=1, null=True, choices = ROLE_CHOICES, verbose_name="نقش", blank=True, default="k")
    position = models.CharField(max_length=1, null=True, choices = POSITION_CHOICES, verbose_name="جایگاه", blank=True, default='c')
    date_created = models.DateTimeField(auto_now_add = True, null=True, verbose_name="تاریخ ایجاد",  blank=True)
    pic = models.ImageField(upload_to="profileimages", null=True, verbose_name="تصویر", default="profileimages/profi.png")
    sphone = models.CharField(max_length=200, null=True, verbose_name="تلفن ثابت", blank=True)
    mphone = models.CharField(max_length=200, null=True, verbose_name="تلفن همراه", blank=True)
    status = models.BooleanField(default=False, verbose_name="درخواست رسانه‌دار شدن")


    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"

    def __str__(self):
        return str(self.company)


    def pic_tag(self):
        return format_html("<img style='width:55px;' src='{}'>".format(self.pic.url))
    pic_tag.short_description = "تصویر"

    def jdate_created(self):
        return jalali_converter(self.date_created)
    jdate_created.short_description = "تاریخ عضویت"
    # def get_absolute_url(self):
    #     return reverse('account:login_register')
