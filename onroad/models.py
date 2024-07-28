from django.db import models
from django.contrib.auth.models import User

# Define ServiceRequest model
class ServiceRequest(models.Model):
    SERVICE_OPTIONS = [
        ('towing', 'Towing'),
        ('tire_replacement', 'Tire Replacement'),
        ('fuel_delivery', 'Fuel Delivery'),
        ('battery_jumpstart', 'Battery Jumpstart'),
        ('flat_tyre', 'Flat Tyre'),
        ('general_services', 'General Services'),
        ('starting_problem', 'Starting Problem'),
        ('fitment_service', 'Fitment Service'),
        ('key_unlock_assistance', 'Key-Unlock Assistance')
    ]

    customer_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    services = models.CharField(max_length=50, choices=SERVICE_OPTIONS)
    location = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=50)
    license_plate_no = models.CharField(max_length=15)
    year = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.services} request by {self.customer_name} for {self.vehicle_model}"

# Define CarServiceRequest model
class CarServiceRequest(ServiceRequest):
    def __str__(self):
        return f"Car Service Request: {super().__str__()}"

# Define BikeServiceRequest model
class BikeServiceRequest(ServiceRequest):
    def __str__(self):
        return f"Bike Service Request: {super().__str__()}"

# Define Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    # def get_bookings(self):
    #     return Booking.objects.filter(profile=self)

# # Define Booking model
# class Booking(models.Model):
#     SERVICE_OPTIONS = [
#         ('towing', 'Towing'),
#         ('tire_replacement', 'Tire Replacement'),
#         ('fuel_delivery', 'Fuel Delivery'),
#         ('battery_jumpstart', 'Battery Jumpstart'),
#         ('flat_tyre', 'Flat Tyre'),
#         ('general_services', 'General Services'),
#         ('starting_problem', 'Starting Problem'),
#         ('fitment_service', 'Fitment Service'),
#         ('key_unlock_assistance', 'Key-Unlock Assistance')
#     ]
    
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     service_type = models.CharField(max_length=30, choices=SERVICE_OPTIONS)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='Pending')

#     def __str__(self):
#         return f"{self.service_type} booking by {self.profile.user.username} on {self.booking_date.strftime('%Y-%m-%d %H:%M:%S')}"

# Define Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

# Define Checkout model
class Checkout(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    payment_status = models.CharField(max_length=20, default='Success')
    created_at = models.DateTimeField(auto_now_add=True)
    booking_status=models.CharField(max_length=20, default='Success')

    def __str__(self):
        return f"Checkout for {self.profile.user.username} - {self.payment_status}-{self.booking_status}"

# # Define BookingSuccess model
# class BookingSuccess(models.Model):
#     booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
#     confirmation_message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Booking success for {self.booking.profile.user.username} - {self.booking.service_type}"
