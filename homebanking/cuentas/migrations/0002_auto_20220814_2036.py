# Generated by Django 3.2.5 on 2022-09-27 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='TipoCuenta',
        ),
    ]
