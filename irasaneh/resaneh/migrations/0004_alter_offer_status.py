# Generated by Django 4.0.2 on 2022-04-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resaneh', '0003_alter_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
    ]
