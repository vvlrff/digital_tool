# Generated by Django 3.2.8 on 2023-04-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='event_place',
            field=models.CharField(default='', max_length=200),
        ),
    ]