# Generated by Django 3.2.7 on 2021-10-04 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globe', '0011_alter_poi_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='subdistrict',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pois', to='globe.subdistrict'),
        ),
    ]