# Generated by Django 3.0.6 on 2020-05-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_roba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roba',
            name='cijena',
            field=models.CharField(max_length=1000),
        ),
    ]