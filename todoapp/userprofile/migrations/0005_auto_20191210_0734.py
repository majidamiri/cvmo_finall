# Generated by Django 2.1.11 on 2019-12-10 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20191210_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
