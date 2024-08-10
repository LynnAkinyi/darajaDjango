from django import forms

class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.IntegerField(label="Amount to Pay")

class PaymentForm(forms.Form):
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'type': 'tel'})
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Amount'})
    )
