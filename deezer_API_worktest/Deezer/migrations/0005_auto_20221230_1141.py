# Generated by Django 3.2.16 on 2022-12-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deezer', '0004_remove_album_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='album',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Publicación'),
        ),
        migrations.AlterField(
            model_name='album',
            name='tracklist',
            field=models.CharField(blank=True, max_length=300, verbose_name='URL del tracklist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='artist',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Publicación'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(blank=True, verbose_name='duración del album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='link',
            field=models.CharField(blank=True, max_length=300, verbose_name='URL de la canción'),
        ),
        migrations.AlterField(
            model_name='song',
            name='picture',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='song',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
