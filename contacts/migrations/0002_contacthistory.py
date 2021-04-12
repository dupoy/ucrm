# Generated by Django 3.1.7 on 2021-04-12 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_history', to='contacts.contact')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_history', to='managers.manager')),
            ],
        ),
    ]