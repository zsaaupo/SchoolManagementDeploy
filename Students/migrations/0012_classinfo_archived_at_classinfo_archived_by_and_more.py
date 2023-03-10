# Generated by Django 4.0.1 on 2022-03-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0011_student_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinfo',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
