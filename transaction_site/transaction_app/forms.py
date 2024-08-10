from django import forms

class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.IntegerField(label="Amount to Pay")
