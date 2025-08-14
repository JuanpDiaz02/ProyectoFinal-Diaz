from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages_list'
    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

class OutboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/outbox.html'
    context_object_name = 'messages_list'
    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'messaging/message_detail.html'
    context_object_name = 'msg'
    def get(self, request, *args, **kwargs):
        resp = super().get(request, *args, **kwargs)
        obj = self.get_object()
        if obj.receiver == request.user and not obj.read:
            obj.read = True
            obj.save()
        return resp

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'
    success_url = reverse_lazy('messaging:outbox')
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    template_name = 'messaging/message_confirm_delete.html'
    success_url = reverse_lazy('messaging:inbox')
    def test_func(self):
        obj = self.get_object()
        return obj.sender == self.request.user or obj.receiver == self.request.user
