# Generated by Django 4.2.8 on 2023-12-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='FIELDNAME',
            new_name='slug',
        ),
    ]
