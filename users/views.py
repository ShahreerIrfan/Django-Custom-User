from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserProfileForm
from django.contrib.auth import login

# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'users/user_registraton.html'
    form_class = UserProfileForm
    success_url = ''
    
    def form_valid(self, form) :
        user = form.save()
        login(user)
        return super().form_valid(form)
