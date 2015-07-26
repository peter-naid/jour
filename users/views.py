from django.shortcuts import render
from django.views.generic import View, FormView, ListView, DetailView, RedirectView
from .models import ImprovedUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegistrationForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect("/users/profile")
        else:
            return super(LoginView, self).get(self.request)

    def post(self, *args, **kwargs):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(username = username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect("/users/profile")
        else:
            return render(self.request, "users/login.html", {"message": "authentication failed", "form":self.form_class})

class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        try:
            logout(self.request)
        except:
            pass
        self.url = "/users/login"
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "users/registration.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect("/users/profile")
        else:
            return super(RegistrationView, self).get(self.request)

    def post(self, *args, **kwargs):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        email = self.request.POST["email"]
        try:
            user = ImprovedUser.objects.create_user(username=username, email=email, password=password)
            return HttpResponseRedirect("/users/login")
        except:
            message = "reqistration failed"
            return render(self.request, "users/registration.html", {"message": message, "form":self.form_class})


# Create your views here.
