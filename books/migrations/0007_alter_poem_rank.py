# Generated by Django 4.0.1 on 2022-01-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_poem_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='rank',
            field=models.FloatField(default=0),
        ),
    ]