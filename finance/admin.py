from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Group, Subgroup, Transaction

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Permissões do sistema", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)

@admin.register(Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    search_fields = ("name", "group__name")
    list_display = ("name", "group")
    list_filter = ("group",)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date", "type", "group", "subgroup", "name", "value", "created_by")
    list_filter = ("type", "group", "subgroup")
    search_fields = ("name", "description")
    date_hierarchy = "date"
