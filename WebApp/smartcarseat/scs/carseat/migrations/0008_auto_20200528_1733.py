# Generated by Django 3.0.3 on 2020-05-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carseat', '0007_auto_20200528_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='safe',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
