from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from .forms import SignupForm
from .models import List


# Create your views here.

class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class HomeView(LoginRequiredMixin, CreateView, ListView):
    # if not logined the redirect to login_url
    login_url = '/login/'

    # model and template_name is members of both CreateView and ListView
    model = List
    template_name = 'home.html'

    # get_queryset is a ListView method that used to filter to_do list  added by the user
    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)

    # both are the members of CreateView and form_valid is used  to insert the added to_do list with the username
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.owner == self.request.user:
            raise Http404
        self.object.delete()
        return redirect(self.success_url)
