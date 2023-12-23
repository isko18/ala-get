# Generated by Django 4.2.3 on 2023-12-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_contact_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СЛУЖБА ПОДДЕРЖКИ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СОЦИАЛЬНЫЕ СЕТИ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title2_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СОЦИАЛЬНЫЕ СЕТИ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title2_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СОЦИАЛЬНЫЕ СЕТИ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СЛУЖБА ПОДДЕРЖКИ'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='СЛУЖБА ПОДДЕРЖКИ'),
        ),
    ]