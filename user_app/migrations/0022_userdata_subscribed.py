# Generated by Django 3.2.3 on 2021-10-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0021_uservendorrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
