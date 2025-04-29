from django.conf import settings
from django.urls import include, path

from app.views import (
    CoMentorCreateView,
    MentorCreateView,
    MentorDeleteView,
    MentorListView,
    MentorUpdateView,
)

urlpatterns = [
    path("", MentorListView.as_view(), name="home"),  # ✅ Home now uses ListView
    path("create/", MentorCreateView.as_view(), name="create_mentor"),  # ✅ Correct
    path(
        "<int:pk>/update/", MentorUpdateView.as_view(), name="update_mentor"
    ),  # ✅ Correct
    path(
        "<int:pk>/delete/", MentorDeleteView.as_view(), name="delete_mentor"
    ),  # ✅ Correct
    path("comentor/create/", CoMentorCreateView.as_view(), name="create-comentor"),
]

# ✅ only include the debug toolbar in DEBUG mode
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
