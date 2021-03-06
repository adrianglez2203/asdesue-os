# Generated by Django 2.1 on 2019-04-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20190419_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('testimonio', models.CharField(max_length=150)),
                ('foto', models.ImageField(upload_to='')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 's',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.AlterModelOptions(
            name='boda',
            options={'ordering': ('fecha_realizacion',), 'verbose_name_plural': 's'},
        ),
    ]
