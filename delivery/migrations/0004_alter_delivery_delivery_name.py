# Generated by Django 4.1.5 on 2023-01-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_rename_title_delivery_delivery_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_name',
            field=models.CharField(max_length=30),
        ),
    ]
