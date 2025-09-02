from django.conf import settings
from django.db import models


class Wallet(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet",
    )
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet({self.user})"


class Transaction(models.Model):
    wallet = models.ForeignKey(
        "payments.Wallet", on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(
        choices=[
            ("deposit", "Deposit"),
            ("withdraw", "Withdraw"),
            ("transfer", "Transfer"),
        ],
        max_length=20,
    )
    status = models.CharField(
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
        default="completed",
        max_length=20,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} {self.amount} ({self.wallet.user})"
