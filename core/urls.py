from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # login/logout prontos do Django
    path("accounts/", include("django.contrib.auth.urls")),

    # sua app
    path("", include("finance.urls")),
]
