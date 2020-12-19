from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from college.models import Notice, Profile, Question, Branch
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http.response import HttpResponseRedirect
from rest_framework import viewsets
from college.myserializer import BranchSerializer, NoticeSerializer

# Create your views here.
# Create your views here.


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
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr",
              "rn", "phone_no", "email", "skills", "myimg", "myresume"]


@method_decorator(login_required, name="dispatch")
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class MyList(TemplateView):
    template_name = "college/mylist.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["notices"] = Notice.objects.all().order_by('-id')[:3]
        context["questions"] = Question.objects.all().order_by('-id')[:3]
        return context


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('-id')
    serializer_class = BranchSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-id')
    serializer_class = NoticeSerializer
    # to search with url ?si='xyz'

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
