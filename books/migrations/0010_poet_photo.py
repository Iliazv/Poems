# Generated by Django 4.0.1 on 2022-11-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_poet_century'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='photo',
            field=models.ImageField(blank=True, upload_to='authors_images/'),
        ),
    ]
