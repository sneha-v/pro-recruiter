# Generated by Django 2.2 on 2019-04-25 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190424_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='pu_percent',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='sslc_percent',
            field=models.FloatField(default=50),
        ),
    ]
