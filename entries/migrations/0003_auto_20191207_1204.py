# Generated by Django 2.2.7 on 2019-12-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20191129_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='approved_contract',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_paymentVerification',
            field=models.ImageField(blank=True, upload_to='payment'),
        ),
    ]
