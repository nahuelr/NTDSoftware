# Generated by Django 4.2.4 on 2023-08-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_manufacturer_vehicle_manufacturers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='pilotConnection',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='pilotConnection',
            field=models.ManyToManyField(blank=True, null=True, to='api.person'),
        ),
    ]
