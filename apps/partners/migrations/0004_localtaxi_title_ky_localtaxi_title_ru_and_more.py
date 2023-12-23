# Generated by Django 4.2.7 on 2023-11-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_rename_patners_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='localtaxi',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
        migrations.AddField(
            model_name='localtaxi',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='become_descriptions_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание СТАТЬ ПАРТНЕРОМ '),
        ),
        migrations.AddField(
            model_name='partners',
            name='become_descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание СТАТЬ ПАРТНЕРОМ '),
        ),
        migrations.AddField(
            model_name='partners',
            name='become_title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок СТАТЬ ПАРТНЕРОМ '),
        ),
        migrations.AddField(
            model_name='partners',
            name='become_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок СТАТЬ ПАРТНЕРОМ '),
        ),
        migrations.AddField(
            model_name='partners',
            name='descriptions_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions2_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions2_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions3_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions3_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='getting_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Что вы получаете'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_descriptions_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_title2_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_title2_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='local_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок Локальный таксопарк'),
        ),
        migrations.AddField(
            model_name='partners',
            name='title2_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='title2_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='title_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
        migrations.AddField(
            model_name='partners',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок партнерство'),
        ),
    ]