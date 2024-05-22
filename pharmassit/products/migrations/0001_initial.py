# Generated by Django 5.0.6 on 2024-05-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('generic_name', models.CharField(max_length=255)),
                ('expiry_date', models.DateField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('storage_loc', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]