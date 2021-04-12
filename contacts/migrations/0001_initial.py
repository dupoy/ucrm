# Generated by Django 3.1.7 on 2021-04-12 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, editable=False, upload_to='')),
                ('type', models.CharField(choices=[('EMAIL', 'Email'), ('PHONE', 'Phone'), ('FACEBOOK', 'Facebook'), ('TELEGRAM', 'Telegram'), ('INSTAGRAM', 'Instagram')], max_length=16)),
                ('value', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='customers.customer')),
            ],
        ),
    ]
