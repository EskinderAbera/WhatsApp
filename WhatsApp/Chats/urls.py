from django.urls import path
from .controller import chatroom_controller
from .controller import message_controller

urlpatterns = [
    path('chatrooms/', chatroom_controller.get_chatroom, name='chatroom-list'),
    path('chatrooms/create/', chatroom_controller.create_chatrooms, name='chatroom-create'),
    # path('chatrooms/<int:chatroom_id>/', chatroom_controller.get_chatroom, name='chatroom-detail'),
    path('chatrooms/leave/<int:chatroom_id>/', chatroom_controller.leave_chatroom, name='chatroom-leave'),
    path('chatrooms/update/<int:chatroom_id>/', chatroom_controller.update_chatroom, name='chatroom-update'),
    path('chatrooms/<int:chatroom_id>/messages/', message_controller.list_messages, name='message-list'),
    path('chatrooms/<int:chatroom_id>/messages/create/', message_controller.create_message, name='create-message'),
    # Add other URLs as needed
]
