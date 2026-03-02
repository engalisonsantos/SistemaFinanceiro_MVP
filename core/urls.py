from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # inclui as rotas do seu sistema
    path("", include("finance.urls")),  # <-- TROQUE "finance" pelo nome real da sua app
]
