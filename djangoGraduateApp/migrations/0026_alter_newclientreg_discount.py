# Generated by Django 5.0.4 on 2024-10-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0025_alter_clientsorders_food_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclientreg',
            name='discount',
            field=models.IntegerField(default=20),
        ),
    ]
