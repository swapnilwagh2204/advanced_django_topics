from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from college import views
from django.views.generic.base import RedirectView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'branch', views.BranchViewSet)
router.register(r'notice', views.NoticeViewSet)


urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('mylist/', views.MyList.as_view()),
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('profile/edit/<int:pk>',
         views.ProfileUpdate.as_view(success_url="/college/home")),
    path('question/create/', views.QuestionCreate.as_view(success_url="/college/home")),

    path(r'api/', include(router.urls)),
    path(r'api-token-auth', obtain_jwt_token),

    path('', RedirectView.as_view(url="home/")),
]
