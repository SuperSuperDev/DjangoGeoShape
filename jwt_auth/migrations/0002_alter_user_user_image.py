# Generated by Django 3.2.7 on 2021-10-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.CharField(default='https://avatars.dicebear.com/api/avataaars/<function random_string at 0x7f4fc831dca0>.svg?size=150', max_length=250),
        ),
    ]