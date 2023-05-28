from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('loanmanage', views.loanmanage, name='loanmanage'),
]

urlpatterns += staticfiles_urlpatterns()