# Generated by Django 2.2.5 on 2019-10-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20191021_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_json',
            field=models.IntegerField(default=0),
        ),
    ]