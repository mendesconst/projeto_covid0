# Generated by Django 3.2.7 on 2022-06-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_premio', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('thumb', models.ImageField(upload_to='thumb_premios')),
            ],
        ),
    ]
