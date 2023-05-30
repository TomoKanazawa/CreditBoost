from django.shortcuts import render
from .forms import LoanAppForm

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def loan_manage(request):
    return render(request, 'myapp/loan_manage.html')

def loan_application(request):
    context = {}
    myform = LoanAppForm()
    if request.POST:
        myform = LoanAppForm(request.POST)
        if myform.is_valid():
            amt = request.POST['loan_amount']
            num_install = request.POST['num_installments']
            print(f"amt = {amt}    num_install = {num_install}")
        else:
            print("Form is not valid. Check your input!")
    context['form'] = myform
    return render(request, 'myapp/loan_application.html', context)

def manage_active_loan(request):
    return render(request, 'myapp/manage_active_loan.html')