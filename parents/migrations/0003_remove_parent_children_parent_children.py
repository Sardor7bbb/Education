# Generated by Django 5.1 on 2024-08-23 12:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_parent_children_alter_parent_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='children',
        ),
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(limit_choices_to={'role': 'User'}, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
    ]