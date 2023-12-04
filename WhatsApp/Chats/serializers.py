from .models import ChatRoom, Message
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'