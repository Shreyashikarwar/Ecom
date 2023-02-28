# Generated by Django 3.2.3 on 2021-11-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0031_rename_vendor_commission_billing_config_admin_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='query',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
