# Generated by Django 3.2.5 on 2021-09-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thailand', '0007_alter_country_validto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]