# Generated by Django 5.0.6 on 2024-05-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tot_price',
            field=models.FloatField(null=True),
        ),
    ]
