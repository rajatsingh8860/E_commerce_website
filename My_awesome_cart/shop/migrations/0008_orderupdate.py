# Generated by Django 2.2.5 on 2019-10-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=200)),
                ('update_desc', models.CharField(max_length=2000)),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
