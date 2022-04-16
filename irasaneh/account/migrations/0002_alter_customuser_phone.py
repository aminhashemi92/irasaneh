# Generated by Django 4.0.2 on 2022-04-15 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(help_text='Enter 10 digits phone number', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='مقدار وارد شده صحیح نمی\u200cباشد', regex='^[0-9]{11}')], verbose_name='Phone Number'),
        ),
    ]