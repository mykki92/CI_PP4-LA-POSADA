# Generated by Django 3.2.21 on 2023-09-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TapasItem',
            fields=[
                ('tapas_id', models.AutoField(primary_key=True, serialize=False)),
                ('tapas_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('tapas_price', models.FloatField()),
                ('plato_price', models.FloatField()),
                ('tapas_type', models.IntegerField(choices=[(0, 'Salads & Cold Cuts'), (1, 'Hot Dishes'), (2, 'Sides')])),
            ],
            options={
                'ordering': ['-tapas_type'],
            },
        ),
    ]