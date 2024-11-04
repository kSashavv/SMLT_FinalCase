# Generated by Django 4.2.13 on 2024-06-30 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_alter_images_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='user',
        ),
        migrations.AddField(
            model_name='imagesmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]