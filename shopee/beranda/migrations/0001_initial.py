# Generated by Django 4.2.1 on 2023-06-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beranda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=40)),
                ('beranda', models.CharField(max_length=35)),
            ],
        ),
    ]