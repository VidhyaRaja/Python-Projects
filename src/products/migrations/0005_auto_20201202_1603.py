# Generated by Django 3.1.4 on 2020-12-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
