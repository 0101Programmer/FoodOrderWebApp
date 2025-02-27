# Generated by Django 5.0.4 on 2024-10-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0012_rename_discount_currentsessionclient_current_session_client_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExistedClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existed_firstname', models.CharField(max_length=40)),
                ('existed_lastname', models.CharField(max_length=40)),
                ('existed_password', models.CharField(max_length=40)),
                ('existed_email', models.EmailField(max_length=40)),
                ('existed_discount', models.IntegerField(default=0)),
            ],
        ),
    ]
