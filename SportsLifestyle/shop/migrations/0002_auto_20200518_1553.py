# Generated by Django 3.0.6 on 2020-05-18 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='naziv',
            new_name='Kategorija',
        ),
        migrations.RenameField(
            model_name='asortiman',
            old_name='kategorija',
            new_name='pol',
        ),
    ]