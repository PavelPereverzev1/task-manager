from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import ListView, TemplateView

from .forms import ProjectForm, TaskForm
from .models import Project, Task


class HomeView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("project-list")
        return super().dispatch(request, *args, **kwargs)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "tasks/project_list.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProjectForm()
        return context

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).prefetch_related("tasks")


class ProjectCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProjectForm()
        return render(request, "tasks/partials/project_form.html", {"form": form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return render(
                request, "tasks/partials/project_card.html", {"project": project}
            )

        return render(
            request, "tasks/partials/project_form.html", {"form": form}, status=422
        )


class ProjectUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk, user=request.user)
        form = ProjectForm(instance=project)
        return render(
            request,
            "tasks/partials/project_form.html",
            {"form": form, "project": project},
        )

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk, user=request.user)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return render(
                request, "tasks/partials/project_card.html", {"project": project}
            )

        return render(
            request,
            "tasks/partials/project_form.html",
            {"form": form, "project": project},
            status=422,
        )


class ProjectDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk, user=request.user)
        project.delete()
        return HttpResponse("")


class TaskCreateView(LoginRequiredMixin, View):
    def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, user=request.user)
        title = request.POST.get("title")
        if title:
            task = Task.objects.create(project=project, title=title)
            return render(request, "tasks/partials/task_item.html", {"task": task})
        return HttpResponse("", status=400)


class TaskToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__user=request.user)
        task.is_completed = not task.is_completed
        task.save()
        return render(request, "tasks/partials/task_item.html", {"task": task})


class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__user=request.user)
        form = TaskForm(instance=task)
        return render(
            request, "tasks/partials/task_form.html", {"form": form, "task": task}
        )

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return render(request, "tasks/partials/task_item.html", {"task": task})
        return render(
            request,
            "tasks/partials/task_form.html",
            {"form": form, "task": task},
            status=422,
        )


class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__user=request.user)
        task.delete()
        return HttpResponse("")
