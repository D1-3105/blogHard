from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts


class MessagesView(ListView):
    template_name = 'home.html'
    model=Posts
    context_object_name = 'messages'
# Create your views here.
