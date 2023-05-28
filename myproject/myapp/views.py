from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def loanmanage(request):
    return render(request, 'myapp/loanmanage.html')