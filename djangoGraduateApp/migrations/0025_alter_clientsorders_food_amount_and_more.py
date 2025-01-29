# Generated by Django 5.0.4 on 2024-10-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0024_alter_clientsorders_client_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsorders',
            name='food_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientsorders',
            name='food_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='firstname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='lastname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='password_confirmation',
            field=models.CharField(max_length=40),
        ),
    ]
