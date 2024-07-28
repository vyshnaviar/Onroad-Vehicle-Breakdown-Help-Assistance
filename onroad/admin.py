from django.contrib import admin
from .models import CarServiceRequest, BikeServiceRequest, Contact, Checkout
@admin.register(CarServiceRequest)
class CarServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_no', 'services', 'location', 'vehicle_model', 'license_plate_no', 'year')

@admin.register(BikeServiceRequest)
class BikeServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_no', 'services', 'location', 'vehicle_model', 'license_plate_no', 'year')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('profile', 'service_type', 'booking_date', 'status')

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('profile', 'payment_status', 'created_at', 'booking_status')  # Corrected here

# @admin.register(BookingSuccess)
# class BookingSuccessAdmin(admin.ModelAdmin):
#     list_display = ('booking', 'confirmation_message', 'created_at')
