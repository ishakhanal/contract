# Generated by Django 2.2.7 on 2019-12-09 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_notification_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='send_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
