from django import forms
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
                }
            ),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "deadline": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
