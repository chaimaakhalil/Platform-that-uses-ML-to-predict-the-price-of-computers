# Generated by Django 4.1.7 on 2023-04-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pouces', models.CharField(max_length=190, null=True)),
                ('Ram', models.CharField(max_length=190, null=True)),
                ('Stockage', models.FloatField(null=True)),
                ('algo', models.CharField(choices=[('GD', 'GD'), ('GS', 'GS')], max_length=190, null=True)),
                ('Poids', models.CharField(max_length=200, null=True)),
                ('Processeur_Intel', models.CharField(max_length=200, null=True)),
                ('Frequence_Processeur', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
