# Generated by Django 5.0.6 on 2024-05-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aspirante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='actaF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='analisisSanguineoF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='certificadoBachilleratoF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='constanciaF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='curpF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='fotoF',
            field=models.IntegerField(null=True),
        ),
    ]
