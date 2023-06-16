# Generated by Django 4.2.2 on 2023-06-07 17:56

import Car_Collection_App.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SPORT_CAR', 'Sports Car'), ('PICKUP', 'Pickup'), ('CROSSOVER', 'Crossover'), ('MINIBUS', 'Minibus'), ('OTHER', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.PositiveIntegerField(validators=[Car_Collection_App.web.models.check_if_year_valid])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
