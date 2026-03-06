from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Cria os grupos básicos de RBAC para o UO Panel"

    def handle(self, *args, **options):
        groups = ["Owner", "Admin", "GM", "ReadOnly"]
        created = []
        existing = []

        for name in groups:
            _, was_created = Group.objects.get_or_create(name=name)
            if was_created:
                created.append(name)
            else:
                existing.append(name)

        if created:
            self.stdout.write(self.style.SUCCESS(f"Grupos criados: {', '.join(created)}"))
        if existing:
            self.stdout.write(self.style.WARNING(f"Grupos já existentes: {', '.join(existing)}"))
        if not created and not existing:
            self.stdout.write("Nenhum grupo processado.")
