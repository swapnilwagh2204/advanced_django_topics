from django.shortcuts import HttpResponse, render
from django.template.response import TemplateResponse

# Create your views here.


def home(request):
    print("i am home view")
    return HttpResponse("hello world")


def excp(request):
    print("i am excp view")
    a = 10/0
    return HttpResponse("hello exp world")


def user_info(request):
    print("i am templaterespnse view")
    context = {'name': 'swapnil'}
    return render(request, 'index.html', context)
