# Generated by Django 4.0.2 on 2022-07-09 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0035_alter_userdata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usr', to=settings.AUTH_USER_MODEL),
        ),
    ]
