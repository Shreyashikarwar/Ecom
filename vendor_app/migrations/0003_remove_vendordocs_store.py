# Generated by Django 3.2.3 on 2021-06-02 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0002_auto_20210601_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendordocs',
            name='store',
        ),
    ]
