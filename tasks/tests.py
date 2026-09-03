from datetime import date, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Project, Task

User = get_user_model()


class TaskManagerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.project = Project.objects.create(title="Work", user=self.user)
        self.task = Task.objects.create(title="Initial Task", project=self.project)

    def test_project_list_status_code(self):
        response = self.client.get(reverse("project-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Work")

    def test_project_create(self):
        response = self.client.post(
            reverse("project-create"),
            {"title": "New Project"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Project.objects.filter(title="New Project", user=self.user).exists()
        )

    def test_project_update(self):
        response = self.client.post(
            reverse("project-update", args=[self.project.id]),
            {"title": "Updated Work"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Updated Work")

    def test_project_delete(self):
        response = self.client.post(
            reverse("project-delete", args=[self.project.id]),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_task_create(self):
        response = self.client.post(
            reverse("task-create", args=[self.project.id]),
            {"title": "New Task"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Task.objects.filter(title="New Task", project=self.project).exists()
        )

    def test_task_toggle_done(self):
        response = self.client.post(
            reverse("task-toggle", args=[self.task.id]),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)

    def test_project_validation_empty_title(self):
        response = self.client.post(
            reverse("project-create"),
            {"title": "   "},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 422)

    def test_task_validation_past_deadline(self):
        past_date = date.today() - timedelta(days=1)
        response = self.client.post(
            reverse("task-update", args=[self.task.id]),
            {
                "title": "Task with past deadline",
                "priority": "medium",
                "deadline": past_date,
            },
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 422)

    def test_user_cannot_access_other_user_project(self):
        other_project = Project.objects.create(title="Secret", user=self.other_user)
        response = self.client.post(
            reverse("project-delete", args=[other_project.id]),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 404)
