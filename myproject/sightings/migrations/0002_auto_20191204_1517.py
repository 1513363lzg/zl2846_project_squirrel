# Generated by Django 2.2.7 on 2019-12-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default=float("nan"), help_text='Age of squirrel', max_length=15),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Latitude',
            field=models.DecimalField(decimal_places=20, help_text='Latitude of squirrel', max_digits=30),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default=float("nan"), help_text='location of squirrel', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Longitude',
            field=models.DecimalField(decimal_places=20, help_text='Longitude of squirrel', max_digits=30),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Primary_fur_color',
            field=models.CharField(choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], default=float("nan"), help_text='Primary fur color of squirrel', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Specific_location',
            field=models.CharField(default=float("nan"), help_text='Specific location of squirrel', max_length=100),
        ),
    ]
