# Generated by Django 3.0.2 on 2020-02-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200224_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='food_id',
            field=models.CharField(max_length=5000),
        ),
    ]