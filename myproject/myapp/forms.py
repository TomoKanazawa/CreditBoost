
from django import forms
from django.core.validators import MinValueValidator
 
# creating a form
class LoanAppForm(forms.Form):
 
    loan_amount = forms.DecimalField(label="Loan Amount ($)", validators=[MinValueValidator(1)])
    num_installments = forms.IntegerField(label="Number of Installments", validators=[MinValueValidator(1)])
