# Generated by Django 4.0.2 on 2022-07-11 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('cities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(default=1, verbose_name='پوزیشن')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='categoryimages', verbose_name='تصویر')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.category', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'نوع رسانه',
                'verbose_name_plural': 'انواع رسانه',
                'ordering': ['parent__id', 'position'],
            },
        ),
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
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('detail', models.TextField(blank=True, verbose_name='توضیحات')),
                ('pcode', models.CharField(blank=True, max_length=200, verbose_name='کد جایگاه')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='آدرس')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='cities.city', verbose_name='شهر')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='cities.country', verbose_name='کشور')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='cities.state', verbose_name='استان')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='cities.zone', verbose_name='منطقه')),
            ],
            options={
                'verbose_name': 'جایگاه',
                'verbose_name_plural': 'جایگاه\u200cها',
                'ordering': ['position'],
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
                ('location', location_field.models.plain.PlainLocationField(blank=True, default='35.69977923732504,411.33733749345987', max_length=63)),
                ('nvisit', models.CharField(blank=True, max_length=200, verbose_name='برآورد بازدید روزانه')),
                ('price', models.PositiveIntegerField(blank=True, default=0, verbose_name='قیمت')),
                ('detail', models.TextField(blank=True, verbose_name='جزییات بیشتر')),
                ('point', models.TextField(blank=True, verbose_name='امتیازات')),
                ('status', models.CharField(choices=[('p', 'فعال'), ('d', 'غیرفعال')], max_length=1, verbose_name='وضعیت')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس صفحه')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='کد شناسایی')),
                ('connectionID', models.CharField(blank=True, max_length=200, verbose_name='کد ارتباطی')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_digital', models.BooleanField(default=False, verbose_name='رسانه\u200cی دیجیتال')),
                ('tvModel', models.CharField(blank=True, max_length=200, verbose_name='مدل تلویزیون')),
                ('tvSize', models.CharField(blank=True, max_length=200, verbose_name='ابعاد تلویزیون')),
                ('is_Androidbox', models.BooleanField(default=False, verbose_name='سیستم\u200cعامل اندروید')),
                ('androidVersion', models.CharField(blank=True, max_length=200, verbose_name='ورژن اندروید')),
                ('operatorNumber', models.CharField(blank=True, max_length=200, verbose_name='تلفن اپراتور')),
                ('category', models.ManyToManyField(blank=True, related_name='resaneh', to='resaneh.Category', verbose_name='نوع رسانه')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='cities.city', verbose_name='شهر')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='account.company', verbose_name='رسانه\u200cدار')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='cities.country', verbose_name='کشور')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('industry', models.ManyToManyField(related_name='resaneh', to='resaneh.Industry', verbose_name='صنعت')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='resaneh.place', verbose_name='گروه رسانه')),
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
            name='StructureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(default=1, verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resaneh.structuretype', verbose_name='زیرشاخه')),
            ],
            options={
                'verbose_name': 'نوع سازه',
                'verbose_name_plural': 'انواع سازه',
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
            field=models.ManyToManyField(blank=True, related_name='resaneh', to='resaneh.ShowType', verbose_name='نوع نمایش'),
        ),
        migrations.AddField(
            model_name='resaneh',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='cities.state', verbose_name='استان'),
        ),
        migrations.AddField(
            model_name='resaneh',
            name='structuretype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='resaneh.structuretype', verbose_name='نوع سازه'),
        ),
        migrations.AddField(
            model_name='resaneh',
            name='tag',
            field=models.ManyToManyField(related_name='resaneh', to='resaneh.Tag', verbose_name='تگ'),
        ),
        migrations.AddField(
            model_name='resaneh',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='cities.zone', verbose_name='منطقه'),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('status', models.BooleanField(default=False, verbose_name='فعال')),
                ('resaneh', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='resanehoffer', to='resaneh.resaneh', verbose_name='رسانه')),
            ],
            options={
                'verbose_name': 'پیشنهاد ویژه',
                'verbose_name_plural': 'پیشنهاد\u200cهای ویژه',
            },
        ),
    ]
