# Generated by Django 4.2.2 on 2023-06-05 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attendees_event', to=settings.AUTH_USER_MODEL),
        ),
    ]