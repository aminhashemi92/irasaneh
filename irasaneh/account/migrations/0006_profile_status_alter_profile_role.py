# Generated by Django 4.0.2 on 2022-04-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_firstname_alter_profile_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=False, verbose_name='درخواست رسانه\u200cدار شدن'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('k', 'رسانه\u200cخواه'), ('b', 'رسانه\u200cدار و رسانه\u200cخواه')], default='k', max_length=1, null=True, verbose_name='نقش'),
        ),
    ]