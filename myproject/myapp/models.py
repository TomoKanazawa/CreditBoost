from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django.db import models


# Create your models here.
class LoanModel(models.Model):
    class LoanStatus(models.TextChoices):
        SUBMITTED = 'Submitted'
        REJECTED = 'Rejected'
        OPEN = 'Open'
        CLOSED = 'Closed'

    profile_id = models.EmailField()
    status = models.CharField(
        max_length=15,
        choices=LoanStatus.choices,
        default=LoanStatus.SUBMITTED,
    )
    initial_loan_amnt = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator({'USD': 1})])
    num_installments = models.IntegerField()
    amt_per_installment = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator({'USD': 1})])
    total_amt_left = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator({'USD': 1})])
    class Meta:
        verbose_name = "loan_app"