# Generated by Django 5.0.4 on 2024-10-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0016_clientsorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsorders',
            name='food_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clientsorders',
            name='food_count',
            field=models.IntegerField(default=0),
        ),
    ]
