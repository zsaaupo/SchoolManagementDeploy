# Generated by Django 4.0.1 on 2022-02-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0008_student_otp_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_by', models.CharField(max_length=255, null=True)),
                ('create_at', models.DateField(null=True)),
                ('create_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateField(null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateField(null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('post_picture', models.ImageField(blank=True, null=True, upload_to='student/post')),
                ('post_text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]