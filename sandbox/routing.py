from django.urls import re_path
from .consumers import (
    ChatRoomConsumer,
    CodeEditorConsumer
)

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi()),
    re_path(r'ws/editor/(?P<room_name>\w+)/$', CodeEditorConsumer.as_asgi()),
]