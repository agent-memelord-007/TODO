# Generated by Django 3.2.9 on 2022-02-24 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_time',
            field=models.DateField(default=datetime.date(2022, 2, 24)),
        ),
    ]
