from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts


class MessagesView(ListView):
    template_name = 'home.html'
    model=Posts
    context_object_name = 'messages'

class MessagesDetailView(DetailView):
    template_name = 'msg_detail_view.html'
    context_object_name = 'msg'
    model=Posts
# Create your views here.
