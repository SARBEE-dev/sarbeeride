# forms.py
from django import forms
from .models import RentalRecord

class AddPaymentForm(forms.ModelForm):
    payment_amount = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = RentalRecord
        fields = ['payment_amount']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


from django import forms

class AddLoanForm(forms.Form):
    loan_amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Add Loan")

class AddRepaymentForm(forms.Form):
    repayment_amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Add Repayment")
