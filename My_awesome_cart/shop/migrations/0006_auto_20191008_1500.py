# Generated by Django 2.2.5 on 2019-10-08 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191008_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='phone_no',
        ),
    ]
