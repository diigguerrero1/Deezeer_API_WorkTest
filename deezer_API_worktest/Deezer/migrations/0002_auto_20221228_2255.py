# Generated by Django 3.2.16 on 2022-12-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deezer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='duration',
            field=models.IntegerField(verbose_name='duración del album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(verbose_name='duración del album'),
        ),
    ]