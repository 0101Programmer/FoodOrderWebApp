# Generated by Django 5.0.4 on 2024-10-21 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoGraduateApp', '0011_currentsessionclient_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentsessionclient',
            old_name='discount',
            new_name='current_session_client_discount',
        ),
    ]
