# Generated by Django 3.2.16 on 2022-12-08 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Dis',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dis',
            new_name='discription',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
