from django.shortcuts import render

def sandbox(request):
    return render(request, 'sandbox/sandbox.html', {'title': 'sandbox'})

def room(request, room_name):
    return render(request, 'sandbox/chatroom.html', {'title': 'room', 'room_name': room_name})

def code_editor(request, room_name):
    return render(request, 'sandbox/code_editor.html', {'title': 'code editor', 'room_name': room_name})