from rest_framework import generics
from conversations.models import Sender, Session, Message
from .serializers import SenderSerializer, SessionSerializer, MessageSerializer

# View for listing all sessions
class SessionListView(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# View for listing all senders
class SenderListView(generics.ListAPIView):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer

# View for listing all messages
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# View for listing all messages given a specific session
class MessageBySessionListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        session_id = self.kwargs['session_id']
        return Message.objects.filter(session_id=session_id)

# View for listing all sessions given a specific sender
class SessionBySenderListView(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        return Session.objects.filter(message__sender_id=sender_id).distinct()
