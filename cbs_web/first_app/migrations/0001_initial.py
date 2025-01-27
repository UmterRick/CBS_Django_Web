# Generated by Django 5.0.6 on 2024-07-11 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('position', models.CharField(choices=[('pilot', 'Pilot'), ('manager', 'Manager'), ('stuart', 'Flight Attendant')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=20)),
                ('seats', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=30)),
                ('departure', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('personal', models.ManyToManyField(to='first_app.employee')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='first_app.plane')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('seat', models.CharField(max_length=5)),
                ('type', models.CharField(choices=[('E', 'Econom'), ('S', 'Standard'), ('F', 'First_clas'), ('B', 'Business')], max_length=15)),
                ('gate', models.PositiveSmallIntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.passenger')),
            ],
        ),
    ]
