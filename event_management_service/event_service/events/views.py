from rest_framework import generics, status
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        # Checking duplicate
        existing_event = Event.objects.filter(
            title=request.data.get("title"),
            date=request.data.get("date"),
            source=request.data.get("source"),
        ).first()

        if existing_event:
            return Response(
                {"detail": "This event already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)
