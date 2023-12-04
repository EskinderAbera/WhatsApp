from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers import MessageSerializer
from ..service.message_service import MessageService
from ..service.chatroom_service import ChatRoomService


@api_view(['GET'])
def list_messages(request, chatroom_id):
    messages = MessageService.get_messages_by_chatroom(chatroom_id)
    serializer = MessageSerializer(messages, many=True)
    # Serialize messages if needed
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_message(request, chatroom_id):
    chatroom = ChatRoomService.get_chatroom_by_id(chatroom_id)
    sender = request.user  # Assuming authentication is set up
    content = request.data.get('content', '')

    message = MessageService.create_message(chatroom, sender, content)
    # Serialize message if needed
    return Response(message)
