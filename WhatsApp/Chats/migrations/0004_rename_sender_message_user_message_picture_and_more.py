# Generated by Django 4.2.8 on 2023-12-04 16:10

import Chats.entity.message
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0003_chatroom_max_count_chatroom_total_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=Chats.entity.message.user_directory_path),
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=Chats.entity.message.user_video_directory_path),
        ),
    ]
