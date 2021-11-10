from .models import Payment, Expense, Account
from django import forms

class PaymentForm(forms.ModelForm):
    
    class Meta:
        model = Payment
        fields = fields = ('__all__')
        
class AccountAddForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('__all__')

class ExpenseAddForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('__all__')