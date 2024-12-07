from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Destination, TravelPackage, Booking, Review
from .forms import BookingForm, ReviewForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class DestinationListView(ListView):
    model = Destination
    template_name = 'destinations/destination_list.html'
    context_object_name = 'destinations'


class PackageDetailView(DetailView):
    model = TravelPackage
    template_name = 'packages/package_detail.html'
    context_object_name = 'package'


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'packages/booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'packages/review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'auth/login.html'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = '/login/'
