# Generated by Django 4.2.8 on 2024-01-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participant',
            fields=[
                ('partici_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='NULL', max_length=20)),
                ('partici_ph', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=200)),
            ],
        ),
    ]
