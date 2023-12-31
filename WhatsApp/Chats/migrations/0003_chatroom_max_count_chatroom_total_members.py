# Generated by Django 4.2.8 on 2023-12-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0002_remove_chatroom_user_chatparticipant'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='max_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='total_members',
            field=models.IntegerField(default=0),
        ),
    ]
