# Generated by Django 3.1.7 on 2021-04-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='Contact phone number', max_length=31),
        ),
    ]
