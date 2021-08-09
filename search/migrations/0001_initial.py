# Generated by Django 3.2.6 on 2021-08-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('growth_form', models.CharField(blank=True, max_length=200)),
                ('care_difficulty', models.CharField(blank=True, max_length=200)),
                ('management_level', models.CharField(blank=True, max_length=200)),
                ('water_period_spring', models.CharField(blank=True, max_length=200)),
                ('water_period_summer', models.CharField(blank=True, max_length=200)),
                ('water_period_autumn', models.CharField(blank=True, max_length=200)),
                ('water_period_winter', models.CharField(blank=True, max_length=200)),
                ('growth_temp', models.CharField(blank=True, max_length=200, null=True)),
                ('sunlight', models.CharField(blank=True, max_length=200, null=True)),
                ('humidity', models.CharField(blank=True, max_length=200, null=True)),
                ('flower', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
