# Generated by Django 5.0.4 on 2024-10-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0021_alter_newclientreg_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclientreg',
            name='discount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='email',
            field=models.EmailField(default='base@mail.ru', max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='firstname',
            field=models.CharField(default='Базовый пользователь', max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='lastname',
            field=models.CharField(default='Базовый пользователь', max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='password',
            field=models.CharField(default='Базовый пользователь', max_length=40),
        ),
        migrations.AlterField(
            model_name='newclientreg',
            name='password_confirmation',
            field=models.CharField(default='Базовый пользователь', max_length=40),
        ),
    ]
