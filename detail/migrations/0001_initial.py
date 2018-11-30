# Generated by Django 2.1.3 on 2018-11-30 07:38

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=2083)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('pickup', models.CharField(default='Aeropuerto', max_length=100)),
                ('plate', models.IntegerField()),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('capacity', models.IntegerField(default=1)),
                ('transmission', models.CharField(default='Mecanica', max_length=20)),
                ('doors', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('color', models.CharField(max_length=20)),
                ('kms', models.IntegerField(default=0)),
                ('pictures', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2083), blank=True, size=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('_id', models.IntegerField(default=967543461)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('token', models.CharField(default='defaultToke', max_length=100)),
                ('uidUser', models.CharField(default='defaultUidUser', max_length=100)),
                ('bookingDate', models.DateField()),
                ('pickup', models.CharField(default='Aeropuerto', max_length=100)),
                ('pickupDate', models.DateField()),
                ('deliverPlace', models.CharField(default='Aeropuerto', max_length=100)),
                ('deliverDate', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Car')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CarRental')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('token', models.CharField(default='defaultToke', max_length=100)),
                ('uidUser', models.CharField(default='defaultUidUser', max_length=100)),
                ('bookingDate', models.DateField()),
                ('pickup', models.CharField(default='Aeropuerto', max_length=100)),
                ('pickupDate', models.DateField()),
                ('deliverPlace', models.CharField(default='Aeropuerto', max_length=100)),
                ('deliverDate', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Car')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CarRental')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CarRental'),
        ),
    ]
