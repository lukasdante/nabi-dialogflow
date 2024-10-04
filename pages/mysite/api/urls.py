from django.urls import path
from .views import (
    SessionListView,
    SenderListView,
    MessageListView,
    MessageBySessionListView,
    SessionBySenderListView,
)

urlpatterns = [
    path('sessions/', SessionListView.as_view(), name='session-list'),
    path('senders/', SenderListView.as_view(), name='sender-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('sessions/<str:session_id>/messages/', MessageBySessionListView.as_view(), name='messages-by-session'),
    path('senders/<str:sender_id>/sessions/', SessionBySenderListView.as_view(), name='sessions-by-sender'),
]
