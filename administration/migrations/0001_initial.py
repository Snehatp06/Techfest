# Generated by Django 4.2.8 on 2024-01-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('program_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=250)),
                ('terms_condition', models.CharField(max_length=300)),
            ],
        ),
    ]
