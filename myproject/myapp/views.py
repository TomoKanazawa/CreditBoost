from .models import LoanModel
from django.shortcuts import render, redirect
from .forms import LoanModelForm

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def loan_manage(request):
    return render(request, 'myapp/loan_manage.html')

def loan_application(request):
    myform = LoanModelForm()
    if request.POST:
        myform = LoanModelForm(request.POST)
        if myform.is_valid():
            request.session['_old_post'] = request.POST
            return redirect('myapp:loan_app_verify')
        else:
            print("Form is not valid. Check your input!")
    return render(request, 'myapp/loan_application.html', {'form' : myform})

def loan_app_verify(request):
    context = {}
    old_post = request.session.get('_old_post')
    form = LoanModelForm(old_post)
    new_loan_app : LoanModel = form.save(commit=False)
    new_loan_app.profile_id = request.user.email
    new_loan_app.amt_per_installment = new_loan_app.initial_loan_amnt / new_loan_app.num_installments
    new_loan_app.total_amt_left = new_loan_app.initial_loan_amnt
    new_loan_app.save()
    context['loan_app'] = new_loan_app
    if request.POST:
        form.save_m2m()
    return render(request, 'myapp/loan_app_verify.html', context)

def manage_active_loan(request):
    return render(request, 'myapp/manage_active_loan.html')