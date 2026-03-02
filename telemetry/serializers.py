from django.utils import timezone
from rest_framework import serializers

from .models import ServerEvent


class EventIngestSerializer(serializers.Serializer):
    event_type = serializers.CharField(max_length=120)
    severity = serializers.ChoiceField(choices=ServerEvent.Severity.choices, default=ServerEvent.Severity.INFO)
    occurred_at = serializers.DateTimeField(required=False)
    payload = serializers.JSONField(required=False, default=dict)

    def create(self, validated_data):
        server = self.context["server"]
        occurred_at = validated_data.get("occurred_at") or timezone.now()
        payload = validated_data.get("payload", {})

        event = ServerEvent.objects.create(
            server=server,
            event_type=validated_data["event_type"],
            severity=validated_data.get("severity", ServerEvent.Severity.INFO),
            occurred_at=occurred_at,
            payload=payload,
        )
        server.last_seen_at = timezone.now()
        server.save(update_fields=["last_seen_at"])
        return event


class RecentServerEventSerializer(serializers.ModelSerializer):
    server = serializers.CharField(source="server.name", read_only=True)

    class Meta:
        model = ServerEvent
        fields = ("id", "server", "event_type", "severity", "occurred_at", "payload", "created_at")
