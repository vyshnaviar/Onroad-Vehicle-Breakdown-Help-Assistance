from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from .forms import RegistrationForm, ProfileForm, UserForm, ContactForm, CarServiceRequestForm, BikeServiceRequestForm,LoginForm
from .models import CarServiceRequest, BikeServiceRequest, Contact, Profile,Checkout
from django.conf import settings

def home(request):
    return render(request, 'onroad/home.html')

def aboutus(request):
    return render(request, 'onroad/aboutus.html')

def services(request):
    return render(request, 'onroad/services.html')

@login_required
def customers(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'onroad/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        
    })


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    
    return render(request, 'onroad/create_profile.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    
    return render(request, 'onroad/login.html', {'form': form})

@login_required
def book_service(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        if service_type == 'car':
            form = CarServiceRequestForm(request.POST)
        else:
            form = BikeServiceRequestForm(request.POST)

        if form.is_valid():
            service_request = form.save()
           
            messages.success(request, 'Service booked successfully!')
            return redirect('service_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CarServiceRequestForm() 

    return render(request, 'onroad/book_service.html', {'form': form})

def service_list(request):
    car_services = CarServiceRequest.objects.all()
    bike_services = BikeServiceRequest.objects.all()
    services = list(car_services) + list(bike_services)
    return render(request, 'onroad/service_list.html', {'services': services})

def service_request(request):
    return render(request, 'service_request.html')

def bike_service_request(request):
    return render(request, 'bike_service_request.html')

def car(request):
    if request.method == 'POST':
        form = CarServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car service request saved successfully!')
            return redirect('checkout')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CarServiceRequestForm()
    return render(request, 'onroad/service_request.html', {'form': form})

def bike(request):
    if request.method == 'POST':
        form = BikeServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bike service request saved successfully!')
            return redirect('checkout')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BikeServiceRequestForm()
    return render(request, 'onroad/bike_service_request.html', {'form': form})

def success_view(request):
    return render(request, 'onroad/success.html')


@login_required
def checkout_view(request):
    if request.method == 'POST':
        
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            
            return redirect('profile_not_found')  

        checkout = Checkout(
            profile=profile,
            
        )
        checkout.save()

        return redirect('success')  
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'onroad/checkout.html', context)

def profile_not_found(request):
    return render(request, 'onroad/profile_not_found.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'onroad/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'onroad/contact_success.html')

def error_view(request):
    return render(request, 'onroad/error.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'onroad/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            messages.success(request, 'User created successfully! Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'onroad/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
