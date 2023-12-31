# Generated by Django 4.2.4 on 2023-08-31 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(max_length=25, unique=True)),
                ('date', models.DateField()),
                ('slot_time', models.TimeField()),
                ('region', models.CharField(blank=True, max_length=255)),
                ('doctor', models.CharField(blank=True, max_length=255)),
                ('appointment_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
