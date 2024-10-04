from django.urls import path
from .views import (
    main_view,
    settings_view,
    develop_view
)

urlpatterns = [
    path('', main_view, name='main'),
    path('settings/', settings_view, name='settings'),
    path('develop/', develop_view, name='develop')
]
