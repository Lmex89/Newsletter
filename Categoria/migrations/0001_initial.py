# Generated by Django 3.2.5 on 2021-07-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateField(null=True)),
            ],
        ),
    ]
