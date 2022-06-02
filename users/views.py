from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Your successfully create an account!'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo-home')
        return super(UserCreateView, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    success_message = 'Your successfully create an account!'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo-home')
