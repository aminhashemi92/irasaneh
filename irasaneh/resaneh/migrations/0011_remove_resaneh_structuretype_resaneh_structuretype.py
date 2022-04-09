# Generated by Django 4.0.2 on 2022-04-08 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resaneh', '0010_structuretype_resaneh_structuretype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resaneh',
            name='structuretype',
        ),
        migrations.AddField(
            model_name='resaneh',
            name='structuretype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resaneh', to='resaneh.structuretype', verbose_name='نوع سازه'),
        ),
    ]
