# Generated by Django 3.2.3 on 2021-09-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0022_homebanner_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVendorCommission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=10.0)),
            ],
            options={
                'db_table': 'UserVendorCommission',
            },
        ),
    ]
