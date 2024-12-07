from django import forms
from .models import Booking, Review, UserProfile


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'travelers']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']
