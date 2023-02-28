# Generated by Django 3.2.3 on 2021-06-17 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0014_auto_20210612_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('ifsc', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payinfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PaymentInfo',
            },
        ),
    ]
