# Generated by Django 2.0 on 2018-03-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status_flag',
            field=models.BooleanField(default=True),
        ),
    ]
