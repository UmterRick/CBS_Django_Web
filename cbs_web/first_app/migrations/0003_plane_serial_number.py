# Generated by Django 5.0.6 on 2024-07-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_passenger_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='serial_number',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]