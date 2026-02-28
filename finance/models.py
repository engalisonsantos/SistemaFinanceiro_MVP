from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from decimal import Decimal


class User(AbstractUser):
    class Role(models.TextChoices):
        MASTER = "MASTER", "Master"
        ENTRY = "ENTRY", "Lançamentos"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ENTRY)

    def is_master(self) -> bool:
        return self.role == self.Role.MASTER


class Group(models.Model):
    class Nature(models.TextChoices):
        RECEITA = "RECEITA", "Receita"
        DESPESA = "DESPESA", "Despesa"

    name = models.CharField(max_length=120, unique=True)
    nature = models.CharField(max_length=10, choices=Nature.choices, default=Nature.RECEITA)

    def __str__(self):
        return f"{self.name} ({self.get_nature_display()})"


class Subgroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="subgroups")
    name = models.CharField(max_length=120)

    class Meta:
        unique_together = ("group", "name")

    def __str__(self):
        return f"{self.group.name} / {self.name}"


class Transaction(models.Model):
    class Type(models.TextChoices):
        PAYMENT = "PAYMENT", "Pagamento"
        RECEIPT = "RECEIPT", "Recebimento"

    type = models.CharField(max_length=10, choices=Type.choices)
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    subgroup = models.ForeignKey(Subgroup, on_delete=models.PROTECT)
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])

    created_by = models.ForeignKey("User", on_delete=models.PROTECT, related_name="created_transactions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.get_type_display()} - {self.name} - R$ {self.value}"

    def save(self, *args, **kwargs):
        # Define automaticamente o tipo conforme a natureza do Grupo
        if self.group.nature == Group.Nature.RECEITA:
            self.type = Transaction.Type.RECEIPT
        else:
            self.type = Transaction.Type.PAYMENT
        super().save(*args, **kwargs)