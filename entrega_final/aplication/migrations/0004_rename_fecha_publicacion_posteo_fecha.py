# Generated by Django 4.2.3 on 2023-08-28 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_remove_posteo_categorias_delete_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteo',
            old_name='fecha_publicacion',
            new_name='fecha',
        ),
    ]