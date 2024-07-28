from django.urls import path
from . import views
from .views import checkout_view, profile_not_found, success_view

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('customers/', views.customers, name='customers'),
    path('profile/', views.customers, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_not_found/', profile_not_found, name='profile_not_found'),
    path('accounts/login/', views.login_view, name='login'),
    path('book_service/', views.book_service, name='book_service'),
    path('service_list/', views.service_list, name='service_list'),
    # path('bike_service_request/', views.bike_service_request, name='bike_service_request'),
    path('checkout/', checkout_view, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('error/', views.error_view, name='error'),
    path('car/', views.car, name='car'),
    path('bike/', views.bike, name='bike'),
   path('success_view/', views.success_view, name='success'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    
]
