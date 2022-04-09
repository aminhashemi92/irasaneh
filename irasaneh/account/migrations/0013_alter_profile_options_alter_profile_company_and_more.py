# Generated by Django 4.0.2 on 2022-03-29 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_profile_mphone_profile_sphone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب\u200cهای کاربری'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(default='profileimages/profi.png', null=True, upload_to='profileimages', verbose_name='لوگو'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('d', 'رسانه\u200cدار'), ('k', 'رسانه\u200cخواه'), ('b', 'رسانه\u200cدار و رسانه\u200cخواه')], max_length=1, null=True, verbose_name='نقش'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
