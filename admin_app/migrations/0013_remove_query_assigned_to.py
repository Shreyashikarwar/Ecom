# Generated by Django 3.2.3 on 2021-06-17 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0012_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='assigned_to',
        ),
    ]
