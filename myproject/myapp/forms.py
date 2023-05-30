
from django.forms import ModelForm, ValidationError
from .models import LoanModel

class LoanModelForm(ModelForm):
    class Meta:
        model = LoanModel
        fields = ['initial_loan_amnt', 'num_installments']
        labels = {'initial_loan_amnt': 'Loan Amount ($)',
                  'num_installments': 'Number of Installments'}
    
    def clean_num_installments(self):
        num_installments = self.cleaned_data.get('num_installments', False)
        if num_installments <= 1:
            raise ValidationError("Number of installments must be greater than 1")
        
        return num_installments
