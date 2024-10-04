from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Sender(models.Model):
    """ Creates a Sender instance. """

    sender_id = models.CharField(max_length=20, primary_key=True, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False, editable=True)


class Session(models.Model):
    """ Creates a Session instance. """

    session_id = models.CharField(max_length=20, primary_key=True, editable=False)

class Message(models.Model):
    """ Creates a Message instance for a unique session. """

    message_id = models.CharField(max_length=20, primary_key=True, editable=False)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(Sender, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False, editable=False)
    date = models.DateTimeField(null=False, blank=False)
    parameters = models.JSONField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()