# Generated by Django 4.1.7 on 2023-04-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_shopping_index_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_index',
            name='img',
            field=models.TextField(default='default_value_here'),
        ),
    ]
