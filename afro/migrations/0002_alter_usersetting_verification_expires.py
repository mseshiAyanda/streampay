# Generated by Django 3.2.5 on 2021-07-29 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersetting',
            name='verification_expires',
            field=models.DateField(default=datetime.date(2021, 8, 1)),
        ),
    ]
