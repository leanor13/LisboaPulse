from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.data.get("added_by"))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    date = filters.DateFilter()
    event_type = filters.CharFilter(lookup_expr="iexact")
    venue = filters.CharFilter(lookup_expr="icontains")
    added_by = filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Event
        fields = ["title", "date", "event_type", "venue", "added_by"]


# TODO: Add filtering by date. also time, date range etc.
# TODO: Add pagination
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter
    ordering_fields = ["date", "title", "event_type", "venue", "added_by"]
    ordering = ["date"]
