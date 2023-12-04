from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from ..serializers import ChatSerializer
from ..service.chatroom_service import ChatRoomService


@api_view(['GET'])
@authentication_classes([BasicAuthentication])  # Applying authentication
@permission_classes([IsAuthenticated])
def list_chatrooms(request):
    chatrooms = ChatRoomService.get_all_chatrooms()
    sender = request.user.id
    # print(sender)
    # Serialize chatrooms if needed
    serializer = ChatSerializer(chatrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_chatroom(request, chatroom_id):
    chatroom = ChatRoomService.get_chatroom_by_id(chatroom_id)
    # Serialize chatroom if needed
    return Response(chatroom)


@api_view(['POST'])
@authentication_classes([BasicAuthentication])  # Applying authentication
@permission_classes([IsAuthenticated])
def create_chatrooms(request):
    # chatroom = ChatRoomService.get_chatroom_by_id(chatroom_id)
    create = request.user  # Assuming authentication is set up
    name = request.data.get('name', '')

    message = ChatRoomService.create_chatroom(name, create)
    # Serialize message if needed
    return Response(message)


@api_view(['PUT'])
@authentication_classes([BasicAuthentication])  # Applying authentication
@permission_classes([IsAuthenticated])
def update_chatroom(request, chatroom_id):
    user = request.user
    # print(user)
    message = ChatRoomService.update_chatroom(chatroom_id, user)
    # Serialize
    return Response(message)