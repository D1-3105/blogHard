from django.urls import path
from .views import MessagesView, MessagesDetailView

urlpatterns = [
    path('', MessagesView.as_view(), name='all_messages'),
    path('msg/<int:pk>', MessagesDetailView.as_view(), name='msg_detail')
]
