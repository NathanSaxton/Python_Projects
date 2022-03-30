# Create your models here.
from django.db import models


class Account(models.Model):
    firstName = models.CharField(max_length=25, default="", blank=True, null=False)
    lastName = models.CharField(max_length=25, default="", blank=True, null=False)
    initialDeposit = models.DecimalField(max_digits=15, decimal_places=2, default="0.00", blank=False, null=False)

    accounts = models.Manager()

    def __str__(self):
        return self.firstName + " " + self.lastName


TransactionTypes = [
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal'),
]


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes, blank=False, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    transactions = models.Manager()

    def __str__(self):
        return self.type + " " + str(self.date)
