# Generated by Django 4.2.4 on 2023-08-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_starship_crew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='MGLT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cargoCapacity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='consumables',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='costInCredits',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='crew',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='hyperdriveRating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='maxAtmospheringSpeed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='starshipClass',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]