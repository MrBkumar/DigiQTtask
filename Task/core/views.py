from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView, FormView, TemplateView
from django.contrib.auth.views import LoginView
from .models import Movie
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from core.utils import MovieData
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('movies')


class RegisterView(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['movies'].count()
        return context

class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name', 'description', 'rating', 'duration', 'release_date']
    success_url = reverse_lazy('movies')

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies')

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')

class LoadData(TemplateView):
    template_name = 'core/load_data.html'

    def get(self, request):
        # load_data = MovieData()
        return render(request, self.template_name)