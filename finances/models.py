from django.db import models
from django.utils import timezone
from blog.models import Student, Staff, School
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
payment_status = (
    ("overpaid", "Overpaid"),
    ("underpaid", "Underpaid"),
    ("payment at par", "Payment Ok"),
   
)

account_name = (
    ("Cash_at_hand", "Cash with Teacher"),
    ("Cash_at_hand", "Cash with Treasurer"),
   
)

transfer_types = (
    ("credit", "Credit"),
    ("debit", "Debit"),
    
)

payment_mode = (
    ("cash", "Cash"),
    ("cheque", "Cheque"),
    ("mpesa", "Mpesa"),
    
)

payable_towards = (
    ("development_fee", "Development Fee"),
    ("motivation_fee", "Motivation Fee"),
    ("exam_fee", "Exam Fee"),
    ("tuition_fee", "Tuition Fee"),
   
)

terms = (
    ("Term 1", "Term 1"),
    ("Term 2", "Term 2"),
    ("Term 3", "Term 3"),
)


class Fee(models.Model):
    term = models.CharField(max_length=100, choices=terms)
    termly_fee = models.IntegerField()

    def __str__(self):
        return str(self.term)


class Payment(models.Model):
    paid_by = models.CharField(max_length=200)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    payable_towards = models.CharField(max_length=200, choices = payable_towards, default = "tuition_fee")
    payment_date =  models.DateTimeField(default=timezone.now)
    amount_paid = models.PositiveBigIntegerField(blank=False, null=True)
    payment_mode = models.CharField(max_length=200, choices = payment_mode, default = "Cash")
    # account_name = models.ForeignKey(Account, on_delete=models.CASCADE, default=70)
    receipt_number = models.IntegerField(blank=False, null=True, unique=True)
    name = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="pay_received_by",)
    # account_balance = models.PositiveBigIntegerField(default=0)
    acc_balance = models.PositiveBigIntegerField(default=0)
    personal_balance = models.IntegerField(default=0)
    term = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=200, default='Underpaid')
    total_pay = models.PositiveBigIntegerField(default=0)
    

# do signal for overpayment to overflow into next term
    def accountBal(self):
        pay_list = Payment.objects.filter(total_pay=self)
        total_pay = 0
        for pay in pay_list:
            total_pay += self.amount_paid
        return self.total_pay + 100

  
    def save(self, **args):
        self.acc_balance = self.acc_balance + self.amount_paid
        self.personal_balance = self.amount_paid - self.term.termly_fee
        #if self.personal_balance:
        #     self.personal_balance = self.amount_paid - self.term.termly_fee
        # else:
        #     self.personal_balance = self.amount_paid - self.personal_balance
        if self.personal_balance > 0:
            self.payment_status = "Overpaid"
            return super().save()
        elif self.personal_balance == 0:
            self.payment_status = "Payment Ok"
            return super().save()
        elif self.personal_balance < 0:
            self.payment_status = "Underpaid"
            return super().save()
        else:
            self.payment_status = "Invalid Payment"
            return super().save()

    def __str__(self):
        return str(self.student_name)

@receiver(post_save, sender=Payment)
def payment_to_account(sender, instance, created,  *args, **kwargs):
    if created:
        print('Payment Created')
        # Payment.acc_balance = Account.balance + instance.amount_paid
        # Account.balance = instance.acc_balance
        
post_save.connect(payment_to_account, sender=Payment)



    
    
    # signal to add payment to account

class Account(models.Model):
    account_name = models.CharField(max_length=200, choices = account_name)
    account_number = models.IntegerField(blank=False, null=True, unique=True)
    opening_balance = models.IntegerField(blank=False, null=True)
    balance = models.IntegerField(blank=False, null=True)
    # acbalance = models.ForeignKey(Payment, on_delete=models.CASCADE)
    # transaction_id = models.UUIDField()

    # def save(self, **args):
    #     self.balance = self.balance + Payment.amount_paid

    def __str__(self):
        return self.account_name

# @property
# def balance_left(self):
#     if (self.balance != None):
#         balance = self.balance + Payment.amount_paid
#         return balance


class Transfers(models.Model):
    transfer_type =models.CharField(max_length=200, choices = transfer_types)
    transaction_amount = models.IntegerField(blank=False, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_by = models.CharField(max_length=200)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return self.transaction_by

class Expense(models.Model):
    expender = models.CharField(max_length=200)
    expense_date = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    expense_amount = models.IntegerField()
    spent_on = models.CharField(max_length=200)
    receipt_number = models.IntegerField(blank=False, null=True, unique=True)
    receipt_photo = models.ImageField(upload_to='receipts', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.expender