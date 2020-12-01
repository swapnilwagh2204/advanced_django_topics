from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from college.models import Notice, Profile, Question
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
# Create your views here.


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "college/index.html"


@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", 'sem', 'marks_10', 'marks_12',
              'marks_aggr', 'rn', 'myimg', 'myresume', 'skills']


class QuestionCreate(CreateView):
    model = Question
    fields = ['subject', 'msg']
