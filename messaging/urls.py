from django.urls import path
from .views import InboxView, OutboxView, MessageDetailView, MessageCreateView, MessageDeleteView

app_name = 'messaging'

urlpatterns = [
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('outbox/', OutboxView.as_view(), name='outbox'),
    path('compose/', MessageCreateView.as_view(), name='compose'),
    path('<int:pk>/', MessageDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='delete'),
]
