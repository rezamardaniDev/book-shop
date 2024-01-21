from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('dashboard', views.profile, name='dashboard'),
]
