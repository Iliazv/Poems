# Generated by Django 4.0.1 on 2022-01-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_poem_poem_name_poem_rating_poem_votes_poet_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
