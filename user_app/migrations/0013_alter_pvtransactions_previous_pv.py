# Generated by Django 3.2.3 on 2021-06-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_alter_userdata_pv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvtransactions',
            name='previous_pv',
            field=models.FloatField(default=0.0),
        ),
    ]
