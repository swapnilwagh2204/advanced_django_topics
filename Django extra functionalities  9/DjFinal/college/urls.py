from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from college import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('about/', views.aboutView.as_view()),
    path('contact/', views.contactView.as_view()),
    path('mylist/', views.MyList.as_view()),
    path('question/create/', views.QuestionCreate.as_view(success_url="/college/home")),
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('profile/edit/<int:pk>',
         views.ProfileUpdateView.as_view(success_url="/college/home")),
    path('', RedirectView.as_view(url="home/")),
]
