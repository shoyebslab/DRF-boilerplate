from django.conf import settings
from django.db import models

from common.models.base import BaseModel


class UserActivityLog(BaseModel):
    """
    Tracks authentication activity (login, logout, token refresh).
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activity_logs",
        null=True,
        blank=True
    )
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User Activity Log"
        verbose_name_plural = "User Activity Logs"

    def __str__(self):
        return f"{self.user} - {self.action} at {self.created_at}"
