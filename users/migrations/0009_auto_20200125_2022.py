# Generated by Django 3.0.2 on 2020-01-25 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20200125_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurents',
            name='email',
        ),
        migrations.RemoveField(
            model_name='restaurents',
            name='password',
        ),
        migrations.AddField(
            model_name='restaurents',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
