# Generated by Django 4.2.7 on 2023-11-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_localtaxi_title_ky_localtaxi_title_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Слайдер партерство',
                'verbose_name_plural': 'Слайдер партерство',
            },
        ),
    ]
