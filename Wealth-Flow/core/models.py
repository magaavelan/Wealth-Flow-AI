from django.db import models
from django.contrib.auth.models import User

class ChatSession(models.Model):
    """Groups individual messages into distinct conversational topics."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, default="New AI Chat Session")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

class ChatMessage(models.Model):
    """Stores every raw user prompt and corresponding AI response message."""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'AI Assistant'),
    ]
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role.capitalize()}: {self.content[:30]}..."