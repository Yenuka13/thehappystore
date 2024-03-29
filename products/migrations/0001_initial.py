# Generated by Django 3.2.8 on 2021-10-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('img_url', models.CharField(max_length=2083)),
                ('download_url', models.CharField(max_length=10000000000000000000000000000000000000)),
            ],
        ),
    ]
