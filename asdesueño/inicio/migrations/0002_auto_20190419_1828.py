# Generated by Django 2.1 on 2019-04-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
