# Generated by Django 2.0 on 2018-05-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0010_comment_last_edit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='repeat',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
