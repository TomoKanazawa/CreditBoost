from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def loan_manage(request):
    return render(request, 'myapp/loan_manage.html')

def loan_application(request):
    return render(request, 'myapp/loan_application.html')

def manage_active_loan(request):
    return render(request, 'myapp/manage_active_loan.html')