from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .auth import ServerKeyAuthentication
from .models import GameServer, ServerEvent
from .serializers import EventIngestSerializer, RecentServerEventSerializer


class IsAuthenticatedServer(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, GameServer)


class EventIngestView(APIView):
    authentication_classes = [ServerKeyAuthentication]
    permission_classes = [IsAuthenticatedServer]

    def post(self, request):
        serializer = EventIngestSerializer(data=request.data, context={"server": request.user})
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        return Response({"ok": True, "event_id": event.id}, status=status.HTTP_201_CREATED)


class RecentEventsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        events = ServerEvent.objects.select_related("server").all()[:200]
        serializer = RecentServerEventSerializer(events, many=True)
        return Response(serializer.data)
