# Generated by Django 4.0.2 on 2022-07-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_send_sms',
            field=models.BooleanField(default=False, verbose_name='ارسال پیامک خوش\u200cآمد'),
        ),
    ]
