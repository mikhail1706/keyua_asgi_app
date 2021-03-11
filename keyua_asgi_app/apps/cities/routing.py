from .consumers import DashboardConsumer

from django.urls import re_path, path

websocket_urlpatterns = [
    path('ws/update/city/<int:user_id>/', DashboardConsumer.as_asgi()),
]