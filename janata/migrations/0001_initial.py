# Generated by Django 3.2.8 on 2022-03-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_code', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
