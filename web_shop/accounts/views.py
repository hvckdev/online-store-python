from django.contrib.auth.views import LoginView
from web_shop.accounts.forms import UserLoginForm
from django.shortcuts import render
from django.views import View


# Create your views here.
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def profile(request):
    return render(request, 'accounts/profile.html')
