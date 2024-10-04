from rest_framework import serializers
from conversations.models import Sender, Session, Message

class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        fields = ['sender_id', 'name']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'session_id', 'sender_id', 'text', 'date', 'parameters']
