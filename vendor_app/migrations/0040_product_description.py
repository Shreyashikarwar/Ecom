# Generated by Django 4.0.2 on 2022-07-12 09:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0039_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
