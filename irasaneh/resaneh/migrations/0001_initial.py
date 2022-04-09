# Generated by Django 4.0.2 on 2022-04-02 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0019_rename_sphone_company_sphone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان صنعت')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس صنعت')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.industry', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'صنعت',
                'verbose_name_plural': 'صنایع',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(default=1, verbose_name='پوزیشن')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='mediatypeimages', verbose_name='تصویر')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.mediatype', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'نوع رسانه',
                'verbose_name_plural': 'انواع رسانه',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Resaneh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام رسانه')),
                ('owner', models.CharField(blank=True, max_length=200, verbose_name='مالک رسانه')),
                ('dimensions', models.CharField(blank=True, max_length=200, verbose_name='ابعاد')),
                ('area', models.CharField(blank=True, max_length=200, verbose_name='مساحت')),
                ('areadetail', models.CharField(blank=True, max_length=200, verbose_name='جزییات مساحت')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='آدرس')),
                ('location', location_field.models.plain.PlainLocationField(blank=True, default=None, max_length=63)),
                ('nvisit', models.CharField(blank=True, max_length=200, verbose_name='برآورد بازدید روزانه')),
                ('price', models.CharField(blank=True, max_length=200, verbose_name='قیمت')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('point', models.TextField(blank=True, verbose_name='امتیازات')),
                ('status', models.CharField(choices=[('p', 'فعال'), ('d', 'غیرفعال')], max_length=1, verbose_name='وضعیت')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس صفحه')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='کد شناسایی')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='account.company', verbose_name='رسانه\u200cدار')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('industry', models.ManyToManyField(related_name='Resanehs', to='resaneh.Industry', verbose_name='صنعت')),
                ('mediatype', models.ManyToManyField(blank=True, to='resaneh.MediaType', verbose_name='نوع رسانه')),
            ],
            options={
                'verbose_name': 'رسانه',
                'verbose_name_plural': 'رسانه\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان تگ')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس تگ')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.tag', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ\u200cها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='ShowType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(default=1, verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.showtype', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'نوع نمایش',
                'verbose_name_plural': 'انواع نمایش',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='ResanehImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='resanehimages', verbose_name='عکس')),
                ('resaneh', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='resanehimage', to='resaneh.resaneh', verbose_name='رسانه')),
            ],
            options={
                'verbose_name': 'عکس\u200cهای رسانه',
                'verbose_name_plural': 'عکس\u200cهای رسانه\u200cها',
            },
        ),
        migrations.AddField(
            model_name='resaneh',
            name='showtype',
            field=models.ManyToManyField(blank=True, to='resaneh.ShowType', verbose_name='نوع نمایش'),
        ),
        migrations.AddField(
            model_name='resaneh',
            name='tag',
            field=models.ManyToManyField(related_name='Resanehs', to='resaneh.Tag', verbose_name='تگ'),
        ),
    ]