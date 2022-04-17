from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="کد")
    class Meta:
        verbose_name = "کشور"
        verbose_name_plural = "کشورها"


    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="کد")
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان‌ها"

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="کد")
    class Meta:
        verbose_name = "شهرستان"
        verbose_name_plural = "شهرستان‌ها"

    def __str__(self):
        return self.name


class Zone(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="کد")
    class Meta:
        verbose_name = "منطقه"
        verbose_name_plural = "مناطق"

    def __str__(self):
        return self.name
