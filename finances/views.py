from django.shortcuts import render, redirect
from .forms import PaymentForm, ExpenseAddForm, AccountAddForm
from django.contrib import messages
from .models import Payment, School
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def payment(request):
    if request.method=='POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # payment_date = form.cleaned_data.get('payment_date')
            # student_name = form.cleaned_data.get('student_name')
            # payable_towards = form.cleaned_data.get('payable_towards')
            # amount_paid = form.cleaned_data.get('amount_paid')
            # account_name = form.cleaned_data.get('account_name')
            # receipt_number = form.cleaned_data.get('receipt_number')
            # paid_by = form.cleaned_data.get('paid_by')
            # name = form.cleaned_data.get('name')
            # payment_mode = form.cleaned_data.get('payment_mode')
            # term = form.cleaned_data.get('term')
            # payment_status = form.cleaned_data.get('payment_status')
            # acc_balance = amount_paid + form.cleaned_data.get('acc_balance')
            # payment_mode = form.cleaned_data.get('payment_mode')
            # account_name = models.ForeignKey(Account, on_delete=models.CASCADE, default=70)
            # account_balance = models.PositiveBigIntegerField(default=0)
            messages.success(request, f'Payment Posted')
            return redirect('paylist')
    else:
        form = PaymentForm()
    return render(request, 'finances/payment.html', {'form':form})



def paylist(request):
    context = {
        'payments': Payment.objects.all()
    }
    return render(request, 'finances/paylist.html', context)

def receipt(request, pk):
    template_path = 'finances/receipt.html'
    context = {
        'receipts': Payment.objects.get(id=pk),
        'schools': School.objects.first()
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error sh0ows some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    


def lastpay(request, id):
    context = {
        'lastpayments': Payment.objects.last()
    }
    return render(request, 'finances/lastpay.html', context)

def payaccount(request, id):
    context = {
        'payaccounts': Payment.objects.filter(id=id)
        # CONSIDER ICONTAINS
    }
    return render(request, 'finances/payaccount.html', context)



def addaccount(request):
    if request.method=='POST':
        form = AccountAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Added')
            return redirect('class')
    else:
        form = AccountAddForm()
    return render(request, 'finances/addaccount.html', {'form':form})


def addexpense(request):
    if request.method=='POST':
        form = ExpenseAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Expense Added')
            return redirect('paylist')
    else:
        form = ExpenseAddForm()
    return render(request, 'finances/addexpense.html', {'form':form})