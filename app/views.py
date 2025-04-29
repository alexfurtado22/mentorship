from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from app.forms import CoMentorForm, CreateMentorForm
from app.models import CoMentor, Mentorship


class MentorListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"  # ✅ Fix: 'templete_name' → 'template_name'
    model = Mentorship
    context_object_name = "mentorships"  # ✅ Define a clear name for template context
    paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:
        search = self.request.GET.get("search")
        queryset = super().get_queryset().filter(user=self.request.user)
        if search:
            queryset = queryset.filter(name__search=search)
        return queryset.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_counts = (
            Mentorship.objects.values("status")
            .annotate(count=Count("status"))
            .order_by("status")
        )

        estagios_flat = [item["status"] for item in status_counts]
        qtd_estagios = [item["count"] for item in status_counts]

        context["estagios_flat"] = estagios_flat
        context["qtd_estagios"] = qtd_estagios
        return context


class MentorCreateView(LoginRequiredMixin, CreateView):
    model = Mentorship
    form_class = CreateMentorForm
    template_name = "app/mentor_create.html"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # 👈 pass user to form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # 👈 set user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        messages.success(
            request, "Mentorship created successfully!", extra_tags="created"
        )
        return super().post(request, *args, **kwargs)


class MentorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mentorship
    form_class = CreateMentorForm
    template_name = "app/mentor_update.html"
    success_url = reverse_lazy("home")
    context_object_name = "mentorship"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # 👈 pass user to form
        return kwargs

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.warning(
            request, "Mentorship update successfully!", extra_tags="update"
        )
        return super().post(request, *args, **kwargs)


class MentorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mentorship
    template_name = "app/mentor_delete.html"
    success_url = reverse_lazy("home")  # ✅ Redirect after success
    context_object_name = "mentorship"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().user

    def post(self, request, *args, **kwargs):
        messages.error(
            request, "Mentorship deleted successfully!", extra_tags="destructive"
        )
        return super().post(request, *args, **kwargs)


class CoMentorCreateView(LoginRequiredMixin, CreateView):
    model = CoMentor
    form_class = CoMentorForm
    template_name = "app/comentor_create.html"
    success_url = reverse_lazy("create_mentor")  # or wherever you want to redirect

    def form_valid(self, form):
        form.instance.user = self.request.user  # ✅ Assign logged-in user
        return super().form_valid(form)
