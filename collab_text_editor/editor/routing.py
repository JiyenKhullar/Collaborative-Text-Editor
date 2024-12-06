from django.urls import re_path
from ..collab_text_editor import consumers

websocket_urlpatterns = [
    re_path(r'ws/editor/$', consumers.TextEditorConsumer.as_asgi()),  # WebSocket URL
]
