# Generated by Django 3.2.25 on 2024-04-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('currentRank', models.IntegerField(blank=True, default=0, null=True)),
                ('previousRrank', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
