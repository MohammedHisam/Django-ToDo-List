# Generated by Django 4.2 on 2023-04-25 22:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='List',
        ),
    ]
