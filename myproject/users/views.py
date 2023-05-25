from django.shortcuts import render

# Create your views here.
from allauth.account.views import SignupView
from django.shortcuts import redirect

class MySignupView(SignupView):
    # Users will be redirectrd to home when they accidentaly click
    # "connect" social account button although it's disables.
    def get_authenticated_redirect_url(self):
        return redirect('myapp:index')

my_signup = MySignupView.as_view()
