# Generated by Django 4.2.8 on 2024-01-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_rename_partici_id_participant_participant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='participant_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
