# Generated by Django 4.2.4 on 2023-08-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_film_planetconnection_film_speciesconnection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='episodeId',
            new_name='episodeID',
        ),
    ]
