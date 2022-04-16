# Generated by Django 4.0.2 on 2022-04-15 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=200, null=True, verbose_name='نام\u200cخانوادگی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('d', 'رسانه\u200cدار'), ('k', 'رسانه\u200cخواه'), ('b', 'رسانه\u200cدار و رسانه\u200cخواه')], default='k', max_length=1, null=True, verbose_name='نقش'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
