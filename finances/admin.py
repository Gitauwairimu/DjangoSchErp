from django.contrib import admin
from .models import School, Fee, Account, Payment, Student, Transfers, Expense


admin.site.site_header = 'School Management System'

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'opening_balance', 'balance')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paid_by', 'student_name', 'payable_towards', 'payment_date', 'amount_paid', 'acc_balance', 'personal_balance', 'total_pay', 'payment_status')

class TransfersAdmin(admin.ModelAdmin):
    list_display = ('transaction_date', 'account', 'transfer_type', 'transaction_amount', 'transaction_by')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_date', 'account', 'receipt_number', 'spent_on', 'expender')

# Register your models here.
admin.site.register(Account, AccountAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Transfers, TransfersAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Fee)


