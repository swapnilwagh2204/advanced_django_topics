from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('college/', include('college.urls')),
    path('accounts/', include('registration.backends.default.urls')),          
    path('', RedirectView.as_view(url="college/")),
]
