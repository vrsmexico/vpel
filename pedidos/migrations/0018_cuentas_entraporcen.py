# Generated by Django 4.0.2 on 2022-03-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0017_cuentas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentas',
            name='entraporcen',
            field=models.BooleanField(default=False),
        ),
    ]