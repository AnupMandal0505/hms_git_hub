# Generated by Django 4.2.4 on 2023-08-31 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.CharField(max_length=50, unique=True)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=50)),
                ('pan', models.CharField(blank=True, max_length=50)),
                ('salary', models.IntegerField()),
                ('signature', models.FileField(default=None, max_length=250, null=True, upload_to='signature/')),
                ('dept_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
