from django.urls import path

from .views import (
    HomeView,
    ProjectListView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,
    TaskCreateView,
    TaskToggleView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path(
        "projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"
    ),
    path(
        "projects/<int:project_id>/tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path("tasks/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]
