# Generated by Django 4.0.2 on 2022-07-11 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('VOD', '0001_initial'),
        ('resaneh', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='advideolog',
            name='resaneh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideolog', to='resaneh.resaneh', verbose_name='رسانه'),
        ),
        migrations.AddField(
            model_name='advideolog',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideolog', to='VOD.advideo', verbose_name='ویدیو'),
        ),
        migrations.AddField(
            model_name='advideocounterlog',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideocounterlog', to='VOD.adbox', verbose_name='باکس'),
        ),
        migrations.AddField(
            model_name='advideocounterlog',
            name='resaneh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideocounterlog', to='resaneh.resaneh', verbose_name='رسانه'),
        ),
        migrations.AddField(
            model_name='advideocounterlog',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideocounterlog', to='VOD.advideo', verbose_name='ویدیو'),
        ),
        migrations.AddField(
            model_name='advideo',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideo', to='account.company', verbose_name='صاحب ویدیو'),
        ),
        migrations.AddField(
            model_name='advideo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideo', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده'),
        ),
        migrations.AddField(
            model_name='advideo',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideo', to='VOD.advideotype', verbose_name='نوع'),
        ),
        migrations.AddField(
            model_name='adevent',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adevent', to='VOD.adbox', verbose_name='باکس'),
        ),
        migrations.AddField(
            model_name='adevent',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adevent', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده'),
        ),
        migrations.AddField(
            model_name='adevent',
            name='resaneh',
            field=models.ManyToManyField(blank=True, related_name='adevent', to='resaneh.Resaneh', verbose_name='رسانه'),
        ),
        migrations.AddField(
            model_name='adconnectionlog',
            name='resaneh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adconnectionlog', to='resaneh.resaneh', verbose_name='رسانه'),
        ),
        migrations.AddField(
            model_name='adbox',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adbox', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده'),
        ),
        migrations.AddField(
            model_name='adbox',
            name='videos',
            field=models.ManyToManyField(related_name='adbox', to='VOD.AdVideo', verbose_name='ویدیوها'),
        ),
        migrations.AddField(
            model_name='adapplicationlog',
            name='resaneh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adapplicationlog', to='resaneh.resaneh', verbose_name='رسانه'),
        ),
    ]
