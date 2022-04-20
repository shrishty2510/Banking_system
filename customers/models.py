from django.db import models

class Transaction(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=130)
    debit_amt = models.IntegerField()
    credit_amt = models.IntegerField()
    account_bal = models.IntegerField()
class Customer(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=130)
    avail_bal = models.IntegerField()


