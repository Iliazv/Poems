# Generated by Django 4.0.1 on 2022-01-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_poem_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='rank',
            field=models.CharField(max_length=10),
        ),
    ]
