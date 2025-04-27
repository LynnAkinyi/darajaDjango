# transaction_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .forms import PaymentForm 

def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            cl = MpesaClient()
            phone_number = form.cleaned_data['phone_number']
            amount = int(form.cleaned_data['amount'])
            account_reference = 'Msupa Cosmetics'
            transaction_desc = 'Payment for Msupa Cosmetics'
            callback_url = 'https://api.darajambili.com/express-payment'

            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            
            # Example response handling
            if response.response_code == '0':  # Replace with the correct attribute or method
                return render(request, 'payment_success.html')
            else:
                return render(request, 'payment_pending.html')
    else:
        form = PaymentForm()  # Initialize an empty form
    return render(request, 'payment_form.html', {'form': form})
