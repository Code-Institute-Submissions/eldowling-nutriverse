# Generated by Django 3.0.7 on 2020-09-12 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_discussions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussions',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='discussions',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
