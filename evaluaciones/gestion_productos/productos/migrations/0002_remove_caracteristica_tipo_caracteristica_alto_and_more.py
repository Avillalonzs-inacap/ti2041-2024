# Generated by Django 5.1 on 2024-10-21 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristica',
            name='tipo',
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='alto',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='ancho',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='peso',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
