# Generated by Django 3.2.21 on 2023-09-16 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_alter_tapasitem_sides_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tapasitem',
            name='sides_price',
        ),
    ]