# Generated by Django 2.2 on 2019-04-18 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190416_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
