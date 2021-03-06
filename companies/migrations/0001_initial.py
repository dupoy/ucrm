# Generated by Django 3.1.7 on 2021-04-15 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(help_text='Contact phone number', max_length=31)),
                ('email', models.EmailField(help_text='Contact email', max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
    ]
