from django.contrib import admin
from .models import Destination, TravelPackage, Booking, Review, UserProfile


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')


@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'destination')
    list_filter = ('destination',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'booking_date', 'status')
    list_filter = ('status',)
    ordering = ('-booking_date',)


admin.site.register(Review)
admin.site.register(UserProfile)
