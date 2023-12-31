# Generated by Django 4.2.7 on 2023-11-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок сайта №1')),
                ('title2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок сайта №2')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание сайта')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото баннера')),
                ('advantage1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущества №1')),
                ('advantage2', models.CharField(blank=True, max_length=255, null=True, verbose_name='преимущества №2')),
                ('advantage3', models.CharField(blank=True, max_length=255, null=True, verbose_name='преимущества №3')),
            ],
        ),
    ]
