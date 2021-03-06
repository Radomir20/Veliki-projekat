# Generated by Django 3.0.6 on 2020-05-18 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200518_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=1000)),
                ('cijena', models.FloatField(max_length=1000)),
                ('slika', models.ImageField(upload_to=None)),
                ('kategorija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Kategorija')),
            ],
        ),
    ]
