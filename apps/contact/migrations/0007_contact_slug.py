# Generated by Django 4.2.7 on 2023-12-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_title_form_ky_contact_title_form_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]