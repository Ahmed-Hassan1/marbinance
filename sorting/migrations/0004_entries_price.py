# Generated by Django 3.2.25 on 2024-04-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorting', '0003_entries_pricechange'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
