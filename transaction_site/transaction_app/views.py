from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .forms import MpesaPaymentForm

def index(request):
    if request.method == 'POST':
        form = MpesaPaymentForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            account_reference = 'reference'
            transaction_desc = 'Payment for goods'
            callback_url = 'https://api.darajambili.com/express-payment'

            cl = MpesaClient()
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse(response)
    else:
        form = MpesaPaymentForm()

    return render(request, 'payment_form.html', {'form': form})
