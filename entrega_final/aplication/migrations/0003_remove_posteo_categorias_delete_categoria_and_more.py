# Generated by Django 4.2.3 on 2023-08-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0002_alter_posteo_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='categorias',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AddField(
            model_name='posteo',
            name='categorias',
            field=models.CharField(default=1231231, max_length=200),
            preserve_default=False,
        ),
    ]