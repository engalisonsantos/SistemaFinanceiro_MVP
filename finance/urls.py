from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_redirect, name="home"),
    path("lancamentos/", views.transactions_view, name="transactions"),
    path("lancamentos/excluir/<int:pk>/", views.transaction_delete, name="transaction_delete"),
    path("api/subgrupos/<int:group_id>/", views.subgroups_by_group, name="subgroups_by_group"),

    # Relatórios (Master)
    path("relatorios/periodo/", views.report_period, name="report_period"),
    path("relatorios/dre/", views.report_dre, name="report_dre"),
]