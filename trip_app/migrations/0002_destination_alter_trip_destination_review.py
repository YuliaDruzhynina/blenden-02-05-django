# Generated by Django 5.0.6 on 2024-06-05 10:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_app.destination'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_app.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
