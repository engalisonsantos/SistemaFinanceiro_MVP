from django.urls import path
from . import views

urlpatterns = [
    # Home do sistema -> manda para transações
    path("", views.home_redirect, name="home"),

    # Tela principal
    path("transactions/", views.transactions_view, name="transactions"),

    # Ações
    path("transactions/<int:pk>/delete/", views.transaction_delete, name="transaction_delete"),
    path("subgroups/<int:group_id>/", views.subgroups_by_group, name="subgroups_by_group"),

    # Relatórios (master)
    path("reports/period/", views.report_period, name="report_period"),
    path("reports/dre/", views.report_dre, name="report_dre"),
]
