from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    # Your other URL patterns
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
]
