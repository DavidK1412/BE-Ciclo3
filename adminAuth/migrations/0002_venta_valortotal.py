# Generated by Django 3.2.8 on 2021-10-18 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='valorTotal',
            field=models.IntegerField(default=0),
        ),
    ]
