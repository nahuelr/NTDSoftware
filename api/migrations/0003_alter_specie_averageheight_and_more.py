# Generated by Django 4.2.4 on 2023-08-19 21:45

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_specie_homeworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specie',
            name='averageHeight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='averageLifespan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='classification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='eyeColors',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=1000, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='specie',
            name='hairColors',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=1000, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='specie',
            name='homeworld',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.planet'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='skinColors',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=1000, null=True, size=None),
        ),
    ]
