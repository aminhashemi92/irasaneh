# Generated by Django 4.0.2 on 2022-07-19 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_is_send_sms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_send_sms',
        ),
    ]
