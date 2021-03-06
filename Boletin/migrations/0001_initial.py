# Generated by Django 3.2.5 on 2021-07-17 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boletin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.URLField(blank=True, null=True)),
                ('target', models.IntegerField(null=True)),
                ('frecuencia', models.IntegerField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votaciones',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('votaciones', models.IntegerField(default=1)),
                ('boletin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Boletin.boletin')),
            ],
        ),
    ]
