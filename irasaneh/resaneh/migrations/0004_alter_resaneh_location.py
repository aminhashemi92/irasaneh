# Generated by Django 4.0.2 on 2022-04-02 19:19

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('resaneh', '0003_alter_resaneh_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resaneh',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63),
        ),
    ]