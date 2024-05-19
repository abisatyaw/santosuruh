from django.urls import path
from . import views


urlpatterns = [
    # path("chat", views.chat_redirect, name="events")
    path("login/", views.login_view, name="login"),
    path("test/", views.test_view, name="test"),
]