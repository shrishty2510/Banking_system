from django.contrib import admin
from . models import Transaction ,Customer

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','name','email','credit_amt','debit_amt','account_bal']

@admin.register(Customer)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['id','name','email','avail_bal']    

