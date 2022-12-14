from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from tasteyourlife.accounts.forms import SignUpForm
from tasteyourlife.accounts.models import Profile

UserModel = get_user_model()


class ProfileView(views.DetailView, LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('sign in'))
        return super().dispatch(request, *args, **kwargs)

    template_name = 'account/profile-details-page.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def profile_edit(request):
    return render(request, 'account/profile-edit-page.html')


class SignUpView(views.CreateView):
    template_name = 'account/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'account/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    template_name = 'account/sign-out.html'


