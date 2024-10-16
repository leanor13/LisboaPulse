from django.urls import path

from .views import EventCreateView, EventDeleteView, EventListView, EventUpdateView

urlpatterns = [
    path("create/", EventCreateView.as_view(), name="event-create"),
    path("list/", EventListView.as_view(), name="event-list"),
    path(
        "update/<int:pk>/", EventUpdateView.as_view(), name="event-update"
    ),  # URL для обновления
    path("delete/<int:pk>/", EventDeleteView.as_view(), name="event-delete"),
]
