# Generated by Django 4.0.1 on 2022-03-02 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Students', '0012_classinfo_archived_at_classinfo_archived_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpost',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentpost',
            name='post_picture',
            field=models.ImageField(upload_to='student/post'),
        ),
        migrations.AlterField(
            model_name='studentpost',
            name='post_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
