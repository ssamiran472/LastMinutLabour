# Generated by Django 3.0.2 on 2020-03-01 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0029_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='communicat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('coustomer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('restaurents_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Restaurents')),
            ],
        ),
    ]
