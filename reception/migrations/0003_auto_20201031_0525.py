# Generated by Django 3.1.2 on 2020-10-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20201031_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupant',
            name='phone',
            field=models.CharField(error_messages={'invalid': 'This phone field must contain only numbers of eleven characters.'}, max_length=11),
        ),
    ]
