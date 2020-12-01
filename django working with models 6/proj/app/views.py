from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app.models import notice

# Create your views here.


def home(request):
    return render(request, 'app/index.html')


# @method_decorator(login_required, name='dispatch')
class noticelistview(ListView):
    model = notice


@method_decorator(login_required, name='dispatch')
class noticedetailview(DetailView):
    model = notice
