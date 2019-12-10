# Generated by Django 2.1.11 on 2019-12-10 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20191210_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='user',
            field=models.ForeignKey(error_messages={'unique': 'A data with that username already exists.'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]