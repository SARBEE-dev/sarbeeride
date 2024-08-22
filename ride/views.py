from django.shortcuts import render, get_object_or_404, redirect
from .models import RentalRecord
from .forms import AddPaymentForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    context = {
        'rentals': RentalRecord.objects.all()
    }
    return render(request, 'land.html', context)

def rental_record_detail(request, pk):
    rental_record = get_object_or_404(RentalRecord, pk=pk)

    if request.method == 'POST':
        form = AddPaymentForm(request.POST)
        if form.is_valid():
            payment_amount = form.cleaned_data['payment_amount']
            rental_record.amount_remaining -= payment_amount
            rental_record.save()
            return redirect('rental_record_detail', pk=rental_record.pk)
    else:
        form = AddPaymentForm()
        payment_currently = rental_record.total_amount - rental_record.amount_remaining

    return render(request, 'rental_record_detail.html', {'rental_record': rental_record, 'form': form, 'pay':payment_currently})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


# views.py
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def custom_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logged_out')
    return render(request, 'logout.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import RentalRecord

'''
def subtract_payment_view(request, pk):
    record = get_object_or_404(RentalRecord, pk=pk)

    if request.method == 'POST':
        payment = int(request.POST.get('payment_amount'))
        if payment > 0:
            record.total_amount += payment
            record.amount_remaining -= record.total_amount
            record.save()
        return redirect('payment_success', pk=record.pk)

    return render(request, 'subtract_payment.html', {'record': record})

'''

from django.shortcuts import render, get_object_or_404, redirect
from .models import RentalRecord

@login_required
def subtract_payment_view(request, pk):
    record = get_object_or_404(RentalRecord, pk=pk)

    if request.method == 'POST':
        payment = int(request.POST.get('payment_amount'))
        if payment > 0:
            record.total_amount += payment
            record.amount_remaining += payment
            record.save()
        return redirect('payment_success', pk=record.pk)

    return render(request, 'subtract_payment.html', {'record': record})



from django.shortcuts import render, get_object_or_404, redirect
from .models import RentalRecord
from .forms import AddLoanForm, AddRepaymentForm

def add_loan_view(request, pk):
    record = get_object_or_404(RentalRecord, pk=pk)

    if request.method == 'POST':
        form = AddLoanForm(request.POST)
        if form.is_valid():
            loan_amount = form.cleaned_data['loan_amount']
            record.total_amount += loan_amount
            record.amount_remaining += loan_amount
            record.save()
            return redirect('rental_record_detail', pk=record.pk)
    else:
        form = AddLoanForm()

    return render(request, 'add_loan.html', {'record': record, 'form': form})

def add_repayment_view(request, pk):
    record = get_object_or_404(RentalRecord, pk=pk)

    if request.method == 'POST':
        form = AddRepaymentForm(request.POST)
        if form.is_valid():
            repayment_amount = form.cleaned_data['repayment_amount']
            if repayment_amount <= record.amount_remaining:
                record.amount_remaining -= repayment_amount
                record.save()
                return redirect('rental_record_detail', pk=record.pk)
            else:
                form.add_error('repayment_amount', 'Repayment amount exceeds remaining amount.')

    else:
        form = AddRepaymentForm()

    return render(request, 'add_repayment.html', {'record': record, 'form': form})
















