# Generated by Django 4.0.5 on 2022-06-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ct_items',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
