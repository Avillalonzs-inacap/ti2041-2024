# Generated by Django 5.1 on 2024-10-21 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caracteristicas', models.ManyToManyField(to='productos.caracteristica')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.marca')),
            ],
        ),
    ]
