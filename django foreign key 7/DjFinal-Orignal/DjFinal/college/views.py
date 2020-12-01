from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from college.models import Notice
from django.views.generic.detail import DetailView

# Create your views here.


def home(req):
    return render(req, "college/index.html")


@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice
