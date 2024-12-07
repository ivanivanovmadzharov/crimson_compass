from django.urls import path
from .views import DestinationListView, PackageDetailView, BookingCreateView, ReviewCreateView
from .views import UserLoginView, UserRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', DestinationListView.as_view(), name='destination-list'),
    path('package/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
    path('book/', BookingCreateView.as_view(), name='book-package'),
    path('review/', ReviewCreateView.as_view(), name='add-review'),
    path('login', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
