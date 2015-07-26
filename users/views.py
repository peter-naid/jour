from django.shortcuts import render
from django.views.generic import View, FormView, ListView, DetailView, RedirectView
from .models import ImprovedUser
from django.contrib.user import authenticate, login
from django.http import HttpResponseRedirect


class LoginView(FormView):
    model = ImprovedUser
    fields = ["username", "password"]

    def post(self, *args, *kwargs):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(username = username, password=password)
        if user is not None and user.is_active:
            login(user)
            return HttpResponseRedirect("/users/profile")
        else:
            return render(self.request, "users/login.html", {"message": "authentication failed"})
            




class LogoutView(RedirectView):


class RegistrationView(FormView):


# Create your views here.
