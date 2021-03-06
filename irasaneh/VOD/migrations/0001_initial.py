# Generated by Django 4.0.2 on 2022-07-11 06:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdApplicationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='AdBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام باکس آگهی')),
                ('numberOfVideos', models.PositiveIntegerField(blank=True, verbose_name='تعداد ویدیوها')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('order', models.CharField(blank=True, help_text='اعداد را به انگلیسی وارد کنید و با - فاصله دهید.', max_length=200, verbose_name='ترتیب نمایش فیلم\u200cها')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('videos_list', models.CharField(blank=True, max_length=200, verbose_name='ویدیو\u200cهای مرتب شده')),
            ],
            options={
                'verbose_name': 'باکس',
                'verbose_name_plural': 'باکس\u200cها',
            },
        ),
        migrations.CreateModel(
            name='AdConnectionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='AdEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('startTime', models.TimeField(default=django.utils.timezone.now, verbose_name='ساعت شروع')),
                ('endTime', models.TimeField(default=django.utils.timezone.now, verbose_name='ساعت پایان')),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع')),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویدادها',
            },
        ),
        migrations.CreateModel(
            name='AdVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام ویدیو')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('video', models.FileField(blank=True, null=True, upload_to='advideos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg'])], verbose_name='ویدیو')),
                ('condition', models.CharField(blank=True, choices=[('p', 'پیش\u200cنویس'), ('d', 'در انتظار بررسی'), ('y', 'تایید شده'), ('n', 'رد شده')], default='p', max_length=1, verbose_name='وضعیت انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ویدیو',
                'verbose_name_plural': 'ویدیوها',
            },
        ),
        migrations.CreateModel(
            name='AdVideoCounterLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
            ],
        ),
        migrations.CreateModel(
            name='AdVideoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='نوع ویدیو')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'نوع ویدیو',
                'verbose_name_plural': 'انواع ویدیو',
            },
        ),
        migrations.CreateModel(
            name='AdVideoLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideolog', to='VOD.adbox', verbose_name='باکس')),
            ],
        ),
    ]
