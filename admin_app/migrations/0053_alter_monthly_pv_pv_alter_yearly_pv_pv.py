# Generated by Django 4.0.2 on 2022-07-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0052_monthly_pv_yearly_pv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_pv',
            name='pv',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='yearly_pv',
            name='pv',
            field=models.FloatField(default=0.0),
        ),
    ]
