from django.urls import path
from .views import *

urlpatterns = [
    path("chat/", chat_view, name="chat"),
]