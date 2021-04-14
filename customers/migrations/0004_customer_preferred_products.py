# Generated by Django 3.1.7 on 2021-04-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0003_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='preferred_products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]