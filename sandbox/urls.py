import code
from django.urls import path
from .views import (
    sandbox,
    room,
    code_editor
)

urlpatterns = [
    path('', sandbox, name="sandbox_home"),
    path('editor/<str:room_name>/', code_editor, name="code_editor"),
    # path('<str:room_name>/', room, name='room')
]