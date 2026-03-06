import secrets

from django.core.management.base import BaseCommand

from telemetry.models import GameServer


class Command(BaseCommand):
    help = "Create a game server or rotate its API key if it already exists."

    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        name = options["name"].strip()
        api_key = secrets.token_hex(32)

        server, created = GameServer.objects.get_or_create(
            name=name,
            defaults={"api_key": api_key, "is_active": True},
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Server '{name}' created."))
        else:
            server.api_key = api_key
            server.is_active = True
            server.save(update_fields=["api_key", "is_active"])
            self.stdout.write(self.style.WARNING(f"Server '{name}' exists. API key rotated."))

        self.stdout.write(f"X-SERVER-KEY: {api_key}")
