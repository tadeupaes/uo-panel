from django.db import models
from django.utils import timezone


class GameServer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    api_key = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    last_seen_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class ServerEvent(models.Model):
    class Severity(models.TextChoices):
        INFO = "info", "Info"
        WARN = "warn", "Warn"
        ERROR = "error", "Error"

    server = models.ForeignKey(GameServer, on_delete=models.CASCADE, related_name="events")
    event_type = models.CharField(max_length=120)
    severity = models.CharField(max_length=16, choices=Severity.choices, default=Severity.INFO)
    occurred_at = models.DateTimeField(default=timezone.now)
    payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-occurred_at", "-id"]
        indexes = [
            models.Index(fields=["-occurred_at"]),
            models.Index(fields=["server", "-occurred_at"]),
            models.Index(fields=["severity", "-occurred_at"]),
            models.Index(fields=["event_type"]),
        ]

    def __str__(self) -> str:
        return f"{self.server.name}::{self.event_type} ({self.severity})"
