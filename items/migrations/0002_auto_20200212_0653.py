# Generated by Django 2.2.7 on 2020-02-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
