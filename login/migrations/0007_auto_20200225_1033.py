# Generated by Django 2.2 on 2020-02-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200219_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='spotify_id',
            field=models.CharField(default='0', max_length=100),
        ),
    ]