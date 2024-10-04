from django.shortcuts import render
from .models import (Sender, Session, Message)
# Create your views here.

def main_view(request):
    """ Main view. """
    
    sessions = Session.objects.all()

    return render(request, 'main.html', {'sessions': sessions})

def settings_view(request):
    """ Settings view. """
    
    sessions = Session.objects.all()

    return render(request, 'settings.html', {'sessions': sessions})

def develop_view(request):
    """ Develop view. """
    
    sessions = Session.objects.all()

    return render(request, 'develop.html', {'sessions': sessions})