# Generated by Django 3.1.2 on 2020-11-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0008_auto_20201102_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
    ]
