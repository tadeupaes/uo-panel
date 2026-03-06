from django.contrib import admin

from .models import GameServer, ServerEvent


@admin.register(GameServer)
class GameServerAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "last_seen_at")
    list_filter = ("is_active",)
    search_fields = ("name", "api_key")
    ordering = ("name",)


@admin.register(ServerEvent)
class ServerEventAdmin(admin.ModelAdmin):
    list_display = ("id", "server", "event_type", "severity", "occurred_at", "created_at")
    list_filter = ("severity", "event_type", "server")
    search_fields = ("server__name", "event_type", "payload")
    readonly_fields = ("created_at",)
    ordering = ("-occurred_at",)
    date_hierarchy = "occurred_at"
