# Generated by Django 3.1.5 on 2021-11-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0002_poll_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='category',
            field=models.DateField(auto_now=True),
        ),
    ]
