from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('loan_application', views.loan_application, name='loan_application'),
  path('manage_active_loan', views.manage_active_loan, name='manage_active_loan'),
  path('loan_manage', views.loan_manage, name='loan_manage'),
]

urlpatterns += staticfiles_urlpatterns()