# Generated by Django 3.1.4 on 2021-02-21 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first', '0004_remove_articles_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='owner',
            field=models.ForeignKey(default='123', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]