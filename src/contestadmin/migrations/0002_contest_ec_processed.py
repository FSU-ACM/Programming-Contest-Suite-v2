# Generated by Django 3.1 on 2020-10-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='ec_processed',
            field=models.BooleanField(default=False),
        ),
    ]