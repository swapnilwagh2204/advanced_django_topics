
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from app import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.home, name='home'),
    path('notice/', views.noticelistview.as_view()),
    path('notice/<int:pk>', views.noticedetailview.as_view()),

]
