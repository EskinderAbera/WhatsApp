from ..models import ChatRoom, ChatParticipant


class ChatRoomRepository:
    @staticmethod
    def get_all_chatrooms():
        return ChatRoom.objects.all()

    @staticmethod
    def get_chatroom_by_id(chatroom_id):
        return ChatRoom.objects.get(pk=chatroom_id)


    @staticmethod
    def create_chatroom(name, user):
        chat_instance = ChatRoom.objects.create(name=name)
        ChatParticipant.objects.create(chat=chat_instance, user=user)
        return chat_instance

    @staticmethod
    def update_chatRoom(chat_id, user):
        chat = ChatRoomRepository.get_chatroom_by_id(chat_id)
        if chat:
            ChatParticipant.objects.create(chat=chat, user=user)
            return chat
        else:
            return None
