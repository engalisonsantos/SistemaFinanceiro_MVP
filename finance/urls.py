from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_redirect, name="home"),
    path("transactions/", views.transactions_view, name="transactions"),
    path("transactions/<int:pk>/delete/", views.transaction_delete, name="transaction_delete"),

    path("api/groups/<int:group_id>/subgroups/", views.subgroups_by_group, name="subgroups_by_group"),

    path("reports/period/", views.report_period, name="report_period"),
    path("reports/dre/", views.report_dre, name="report_dre"),
]
