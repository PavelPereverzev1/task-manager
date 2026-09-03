from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "created_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "user__username")
    list_filter = ("created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "project",
        "priority",
        "deadline",
        "is_completed",
    )
    list_display_links = ("id", "title")
    list_filter = ("is_completed", "priority", "project")
    search_fields = ("title", "project__title")
    list_editable = ("is_completed", "priority")
