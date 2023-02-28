# Generated by Django 3.2.3 on 2021-10-08 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0023_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memberip_Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(auto_now=True)),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Memberip_Receipt',
            },
        ),
    ]
