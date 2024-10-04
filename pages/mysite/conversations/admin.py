from django.contrib import admin
from .models import (Sender, Session, Message)

# Register your models here.
admin.site.register(Sender)
admin.site.register(Session)
admin.site.register(Message)