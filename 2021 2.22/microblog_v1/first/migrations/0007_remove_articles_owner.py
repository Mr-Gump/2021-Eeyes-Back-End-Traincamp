# Generated by Django 3.1.4 on 2021-02-22 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20210222_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='owner',
        ),
    ]
