from django.conf.urls import include, url
from .views import LoginView, LogoutView, RegistrationView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='users_login'),
    url(r'^logout/$', LogoutView.as_view(), name='users_logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='user_registration'),
]
