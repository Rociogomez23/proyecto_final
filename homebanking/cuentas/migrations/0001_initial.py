# Generated by Django 3.2.5 on 2022-09-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_subname', models.TextField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('branch_id', models.IntegerField(blank=True, null=True)),
                ('customer_type_id', models.IntegerField(blank=True, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('account_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_type_description', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': False,
            },
        ),
    ]
