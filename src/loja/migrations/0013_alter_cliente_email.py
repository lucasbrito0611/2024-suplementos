# Generated by Django 5.1 on 2024-09-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0012_remove_cliente_dt_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Email',
            field=models.EmailField(max_length=100),
        ),
    ]
