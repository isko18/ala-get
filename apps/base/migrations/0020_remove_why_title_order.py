# Generated by Django 4.2.7 on 2023-11-11 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_orderсity_title_order_why_title_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='why',
            name='title_order',
        ),
    ]
