# Generated by Django 2.2.7 on 2019-12-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.DecimalField(decimal_places=2, help_text='Latitude of squirrel', max_digits=30)),
                ('Longitude', models.DecimalField(decimal_places=2, help_text='Longitude of squirrel', max_digits=30)),
                ('Unique_squirrel_ID', models.CharField(help_text='Unique squirrel id', max_length=50)),
                ('Hectare', models.CharField(help_text='Hectare of squirrel,like 32D', max_length=10)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift of squirrel', max_length=15)),
                ('Date', models.DateField(help_text='Date', null=True)),
                ('Hectare_squirrel_num', models.SmallIntegerField(help_text='number within the chronological sequence of squirrel sightings')),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default=float("nan"), help_text='Age of squirrel', max_length=15)),
                ('Primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], default=float("nan"), help_text='Primary fur color of squirrel', max_length=20)),
                ('Location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default=float("nan"), help_text='location of squirrel', max_length=20)),
                ('Specific_location', models.CharField(default=float("nan"), help_text='Specific location of squirrel', max_length=100)),
                ('Running', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Running', max_length=5, null=True)),
                ('Chasing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Chasing', max_length=5, null=True)),
                ('Climbing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Climbing', max_length=5, null=True)),
                ('Eating', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Eating', max_length=5, null=True)),
                ('Foraging', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Foraging', max_length=5, null=True)),
                ('Other_Activities', models.CharField(blank=True, help_text='Does squirrel have other activities?', max_length=100, null=True)),
                ('Kuks', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Kuks', max_length=5, null=True)),
                ('Quaas', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Quaas', max_length=5, null=True)),
                ('Moans', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Moans', max_length=5, null=True)),
                ('Tail_Flags', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Tail flags', max_length=5, null=True)),
                ('Tail_Twitches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Tail twitches', max_length=5, null=True)),
                ('Approaches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Approaches', max_length=5, null=True)),
                ('Indifferent', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Indifferent', max_length=5, null=True)),
                ('Runs_From', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', help_text='Runs from', max_length=5, null=True)),
            ],
        ),
    ]
