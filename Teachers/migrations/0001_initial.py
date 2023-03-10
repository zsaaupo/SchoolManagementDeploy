# Generated by Django 4.0 on 2022-01-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Other')], max_length=6)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Buddha', 'Buddha')], max_length=10)),
                ('birth_date', models.DateField()),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Widowed', 'Widowed')], max_length=10, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('address', models.TextField()),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('A-', 'A-'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('none', 'none')], default='none', max_length=4)),
                ('nationality', models.CharField(default='Bangladeshi', max_length=50)),
            ],
        ),
    ]
