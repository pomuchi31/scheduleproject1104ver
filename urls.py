from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("workschedule.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workschedule/', include('workschedule.urls')),
]
