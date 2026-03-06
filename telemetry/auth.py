from rest_framework import authentication
from rest_framework import exceptions

from .models import GameServer


class ServerKeyAuthentication(authentication.BaseAuthentication):
    header_name = "HTTP_X_SERVER_KEY"

    def authenticate(self, request):
        api_key = request.META.get(self.header_name)
        if not api_key:
            return None

        try:
            server = GameServer.objects.get(api_key=api_key, is_active=True)
        except GameServer.DoesNotExist as exc:
            raise exceptions.AuthenticationFailed("Invalid or inactive server key.") from exc

        return (server, None)

    def authenticate_header(self, request):
        return "X-SERVER-KEY"
