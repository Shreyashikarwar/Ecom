# Generated by Django 4.0.2 on 2022-07-12 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0047_alter_aboutus_content_alter_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='content',
        ),
    ]
