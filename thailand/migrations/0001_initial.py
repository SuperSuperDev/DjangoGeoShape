# Generated by Django 3.2.5 on 2021-08-03 00:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='thailandPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm0_en', models.CharField(max_length=50)),
                ('adm0_th', models.CharField(max_length=50)),
                ('adm0_pcode', models.CharField(max_length=50)),
                ('adm1_en', models.CharField(max_length=50)),
                ('adm1_th', models.CharField(max_length=50)),
                ('adm1_pcode', models.CharField(max_length=50)),
                ('adm2_en', models.CharField(max_length=50)),
                ('adm2_th', models.CharField(max_length=50)),
                ('adm2_pcode', models.CharField(max_length=50)),
                ('adm3_en', models.CharField(max_length=50)),
                ('adm3_th', models.CharField(max_length=50)),
                ('adm3_pcode', models.CharField(max_length=50)),
                ('adm3_ref', models.CharField(default='', max_length=50)),
                ('adm3alt1en', models.CharField(default='', max_length=50)),
                ('adm3alt2en', models.CharField(default='', max_length=50)),
                ('adm3alt1th', models.CharField(default='', max_length=50)),
                ('adm3alt2th', models.CharField(default='', max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='thailandShapes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_leng', models.FloatField()),
                ('admlevel', models.IntegerField()),
                ('date', models.DateField()),
                ('validon', models.DateField()),
                ('validto', models.DateField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
    ]