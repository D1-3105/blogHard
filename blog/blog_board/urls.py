from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('', MessagesView.as_view(), name='posts_messages_user')
]
