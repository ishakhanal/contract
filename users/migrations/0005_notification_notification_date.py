# Generated by Django 2.2.7 on 2019-12-09 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
