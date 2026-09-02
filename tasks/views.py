from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import ListView, TemplateView

from .forms import ProjectForm
from .models import Project


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


class ProjectDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk, user=request.user)
        project.delete()
        return HttpResponse("")
