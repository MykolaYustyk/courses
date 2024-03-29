# Generated by Django 4.1.5 on 2023-01-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_id', models.BigIntegerField(max_length=10)),
                ('discription', models.TextField(max_length=200)),
                ('brand', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=30)),
                ('product_link', models.CharField(max_length=150)),
            ],
        ),
    ]
