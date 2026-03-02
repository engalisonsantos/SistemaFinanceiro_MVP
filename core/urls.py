from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# View simples para teste (pode remover depois)
def home(request):
    return HttpResponse("Sistema Financeiro rodando com sucesso 🚀")


urlpatterns = [
    path("admin/", admin.site.urls),

    # Página inicial
    path("", home, name="home"),

    # Se você tiver apps, adicione aqui:
    # path("financeiro/", include("financeiro.urls")),
]
