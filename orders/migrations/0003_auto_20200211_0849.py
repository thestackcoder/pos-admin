# Generated by Django 2.2.7 on 2020-02-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_balancecheck_earnings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balancecheck',
            name='petty',
        ),
        migrations.AddField(
            model_name='balancecheck',
            name='petty_cash',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='balancecheck',
            name='pos_id',
            field=models.CharField(default=123456, max_length=50),
            preserve_default=False,
        ),
    ]
