# Generated by Django 4.0.6 on 2022-07-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price_ask',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='price',
            name='price_bid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]