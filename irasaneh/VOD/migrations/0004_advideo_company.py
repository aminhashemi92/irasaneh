# Generated by Django 4.0.2 on 2022-06-22 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('VOD', '0003_advideotype_alter_advideo_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='advideo',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advideo', to='account.company', verbose_name='رسانه\u200cدار'),
        ),
    ]
