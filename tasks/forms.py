from django import forms
from django.utils import timezone
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter list name...",
                    "required": True,
                    "maxlength": "255",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Project title cannot be empty.")
        return title


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "priority", "deadline"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Task title...",
                    "required": True,
                    "maxlength": "255",
                }
            ),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "min": timezone.now().strftime("%Y-%m-%d"),
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Task title cannot be empty.")
        return title

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < timezone.now().date():
            raise forms.ValidationError("Deadline cannot be in the past.")
        return deadline
