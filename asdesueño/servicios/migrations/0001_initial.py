# Generated by Django 2.1 on 2019-04-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio_Boda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=35)),
                ('Descripcion', models.CharField(max_length=255)),
            ],
        ),
    ]
