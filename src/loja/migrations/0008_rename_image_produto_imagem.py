# Generated by Django 5.1 on 2024-09-02 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_produto_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='image',
            new_name='Imagem',
        ),
    ]