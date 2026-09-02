from django.urls import path

from .views import (
    HomeView,
    ProjectListView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path(
        "projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"
    ),
]
