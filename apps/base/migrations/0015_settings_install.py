# Generated by Django 4.2.7 on 2023-11-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_settings_made_descriptions_settings_made_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='install',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Установить приложение'),
        ),
    ]
