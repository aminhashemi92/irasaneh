# Generated by Django 4.0.2 on 2022-04-01 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_rename_sphone_profile_sphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='sPhone',
            new_name='sphone',
        ),
    ]
