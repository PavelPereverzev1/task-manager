from django.urls import path

from .views import HomeView, ProjectListView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
]
