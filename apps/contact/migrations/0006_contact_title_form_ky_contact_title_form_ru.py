# Generated by Django 4.2.7 on 2023-11-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contact_title_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title_form_ky',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=' Заголовок формы'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_form_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=' Заголовок формы'),
        ),
    ]