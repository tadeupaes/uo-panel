from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameServer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("api_key", models.CharField(max_length=64, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("last_seen_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="ServerEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_type", models.CharField(max_length=120)),
                (
                    "severity",
                    models.CharField(
                        choices=[("info", "Info"), ("warn", "Warn"), ("error", "Error")],
                        default="info",
                        max_length=16,
                    ),
                ),
                ("occurred_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("payload", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "server",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="telemetry.gameserver",
                    ),
                ),
            ],
            options={
                "ordering": ["-occurred_at", "-id"],
                "indexes": [
                    models.Index(fields=["-occurred_at"], name="telemetry_s_occurre_0410ff_idx"),
                    models.Index(fields=["server", "-occurred_at"], name="telemetry_s_server__e13cde_idx"),
                    models.Index(fields=["severity", "-occurred_at"], name="telemetry_s_severit_eedec9_idx"),
                    models.Index(fields=["event_type"], name="telemetry_s_event_t_34ac67_idx"),
                ],
            },
        ),
    ]
