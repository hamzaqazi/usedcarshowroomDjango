# Generated by Django 3.2.3 on 2021-07-10 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name', max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(help_text='Your phone number', max_length=250)),
                ('message', models.TextField(help_text='Your message')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No details available', help_text='Toyota yaris', max_length=40)),
                ('short_description', models.TextField(default='No details available', max_length=500)),
                ('long_description', models.TextField(default='No details available', max_length=900)),
                ('price', models.CharField(default='No details available', max_length=255)),
                ('model_year', models.IntegerField(default='No details available', help_text='2017')),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Bio-Diesel', 'Bio-Diesel'), ('Compressed Natural Gas (CNG)', 'Compressed Natural Gas (CNG)')], default='No details available', max_length=40)),
                ('mileage', models.CharField(default='No details available', help_text='21,000', max_length=255)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Continuously variable', 'Continuously variable'), ('Semi-automatic and dual-clutch', 'Semi-automatic and dual-clutch')], default='No details available', max_length=40)),
                ('engine_size', models.CharField(default='No details available', help_text='2.7L', max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('listed_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_style', models.CharField(default='No details available', help_text='Hatchback', max_length=255)),
                ('engine_size', models.CharField(default='No details available', help_text='1299 cc', max_length=255)),
                ('fuel_type', models.CharField(default='No details available', help_text='Petrol', max_length=255)),
                ('number_of_doors', models.IntegerField(default='No details available', help_text='5 doors')),
                ('number_of_seats', models.IntegerField(default='No details available', help_text='5 seats')),
                ('gearbox_type', models.CharField(default='No details available', help_text='semi-automatic', max_length=255)),
                ('CO2_emissions', models.CharField(default='No details available', help_text='136 g/km', max_length=255)),
                ('insurance_group', models.CharField(default='No details available', help_text='06E', max_length=255)),
                ('standard_manufacturer_warranty_miles', models.CharField(default='No details available', help_text='60000 miles', max_length=255)),
                ('standard_manufacturer_warranty_years', models.CharField(default='No details available', help_text='4 years', max_length=255)),
                ('standard_paintwork_guarantee', models.CharField(default='No details available', help_text='3 years', max_length=255)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSafety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety', models.CharField(default='No details available', help_text='Air Bag', max_length=250)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePerformanceEconomy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_consumption_urban', models.CharField(default='No details available', help_text='42.2 mpg', max_length=250)),
                ('fuel_consumption_extra_urban', models.CharField(default='No details available', help_text='42.2 mpg', max_length=250)),
                ('fuel_consumption_combined', models.CharField(default='No details available', help_text='42.2 mpg', max_length=250)),
                ('zero_to_sixty_mph', models.CharField(default='No details available', help_text=' 13.1 seconds', max_length=250)),
                ('top_speed', models.CharField(default='No details available', help_text='106 mph', max_length=250)),
                ('cylinders', models.CharField(default='No details available', help_text='4', max_length=250)),
                ('valves', models.CharField(default='No details available', help_text='16', max_length=250)),
                ('engine_power', models.CharField(default='No details available', help_text='85 bhp', max_length=250)),
                ('engine_torque', models.CharField(default='No details available', help_text='89.25 lbs/ft', max_length=250)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior', models.CharField(default='No details available', help_text='Air-Conditioning', max_length=250)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInquirie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='Name', help_text='Your name', max_length=250)),
                ('customer_email', models.EmailField(max_length=250)),
                ('customer_phone', models.CharField(help_text='Phone', max_length=250)),
                ('customer_message', models.TextField(help_text='Your message')),
                ('inquiry_date', models.DateField(auto_now_add=True)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleExterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exterior', models.CharField(default='No details available', help_text='Spare Wheel', max_length=250)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(default='No details available', help_text='1530 mm', max_length=250)),
                ('height_inclusive_of_roof_rails', models.CharField(default='No details available', max_length=250)),
                ('length', models.CharField(default='No details available', help_text='1530 mm', max_length=250)),
                ('wheelbase', models.CharField(default='No details available', help_text='2430 mm', max_length=250)),
                ('width', models.CharField(default='No details available', help_text='1665 mm', max_length=250)),
                ('width_icluding_mirrors', models.CharField(default='No details available', help_text='1960 mm', max_length=250)),
                ('fuel_tank_capacity', models.CharField(default='No details available', help_text='42 litres', max_length=250)),
                ('minimum_kerb_weight', models.CharField(default='No details available', help_text='1010 kg', max_length=250)),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
