# Generated by Django 3.2.3 on 2021-07-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0018_auto_20210630_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwithdrawrequest',
            name='tds',
            field=models.FloatField(default=0.0),
        ),
    ]
