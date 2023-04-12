# Generated by Django 4.1.7 on 2023-04-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_detail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TextField()),
                ('uniq_id', models.TextField()),
                ('manufacturer', models.TextField()),
                ('price', models.FloatField()),
                ('average_review_rating', models.TextField()),
                ('city', models.TextField()),
                ('country', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.shopping_index')),
            ],
        ),
    ]