# Generated by Django 5.2.1 on 2025-05-31 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='FormSubmission',
        ),
    ]
