# Generated by Django 3.2.3 on 2021-06-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_razorpayorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazorpayTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'RazorpayTransaction',
            },
        ),
        migrations.AddField(
            model_name='razorpayorder',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
