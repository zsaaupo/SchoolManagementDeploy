# Generated by Django 4.0.1 on 2022-03-02 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0010_alter_classinfo_student_alter_guardianinfo_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fee',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
