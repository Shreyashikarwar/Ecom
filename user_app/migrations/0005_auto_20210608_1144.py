# Generated by Django 3.2.3 on 2021-06-08 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0008_auto_20210605_1134'),
        ('user_app', '0004_cart_cartitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productcolor', to='vendor_app.productcolors'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productsize', to='vendor_app.productsizes'),
        ),
    ]
