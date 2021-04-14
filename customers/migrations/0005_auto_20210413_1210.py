# Generated by Django 3.1.7 on 2021-04-13 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20210409_1122'),
        ('customers', '0004_customer_preferred_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='companies.company'),
        ),
    ]