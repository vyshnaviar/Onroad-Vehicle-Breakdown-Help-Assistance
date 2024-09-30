from django import forms
from django.core.exceptions import ValidationError
from .models import CarServiceRequest, BikeServiceRequest, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm
from .validators import validate_password
import re

def validate_phone_number(value):
    if not re.match(r'^\d{10,12}$', value):
        raise ValidationError('Enter a valid phone number with 10 to 12 digits.')
    
def validate_location(value):
    if not re.match(r'^[A-Za-z0-9\s]+$', value):
        raise ValidationError('Enter a valid location with only letters, numbers, and spaces.')
    
def validate_vehicle_model(value):
    if len(value) < 3:
        raise ValidationError('Vehicle model must be at least 3 characters long.')
    if not re.search(r'[A-Za-z]', value):
        raise ValidationError('Vehicle model must contain alphabets.')
    if not (re.search(r'[A-Za-z]', value) and re.search(r'[0-9]', value)) and not value.isalpha():
        raise ValidationError('Vehicle model must contain both alphabets and numbers or alphabets only.')


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password", validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3 or not re.match("^[A-Za-z]*$", first_name):
            raise forms.ValidationError('First name must contain at least 3 letters and only letters!')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match("^[A-Za-z]*$", last_name):
            raise forms.ValidationError('Last name should contain only letters.')
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            raise forms.ValidationError('Invalid email format!')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists!')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) <= 3 or not re.match("^[A-Za-z]*$", username):
            raise forms.ValidationError('Username must contain only letters and be more than 3 characters long!')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists!')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            # Save the Profile model instance
            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number'),
                address=self.cleaned_data.get('address')
            )
        return user

def validate_year(value):
    try:
        year = int(value)
    except ValueError:
        raise ValidationError('Year must be a number.')
    if not (1990 <= year <= 2024):
        raise ValidationError('Year must be between 1990 and 2024.')

def validate_license_plate(value):
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,8}$', value):
        raise ValidationError('License plate must be 6 to 8 characters long and contain both letters and digits.')
    


class CarServiceRequestForm(forms.ModelForm):
    year = forms.CharField(max_length=4, validators=[validate_year], widget=forms.TextInput(attrs={'type': 'text'}))

    class Meta:
        model = CarServiceRequest
        fields = ['customer_name', 'phone_no', 'services', 'location', 'vehicle_model', 'license_plate_no', 'year']

    def clean_customer_name(self):
        customer_name= self.cleaned_data.get('customer_name')
        if len(customer_name) < 4 or not customer_name.isalpha():
            raise ValidationError('Customer must be at least 4 letters and contain letters only.')
        return customer_name

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        validate_phone_number(phone_no)
        return phone_no
    
    

    def clean_license_plate_no(self):
        license_plate_no = self.cleaned_data.get('license_plate_no')
        validate_license_plate(license_plate_no)
        return license_plate_no

    def clean_year(self):
        year = self.cleaned_data.get('year')
        validate_year(year)
        return year

    def clean_vehicle_model(self):
        vehicle_model = self.cleaned_data.get('vehicle_model')
        validate_vehicle_model(vehicle_model)
        return vehicle_model

class BikeServiceRequestForm(forms.ModelForm):
    year = forms.CharField(max_length=4, validators=[validate_year], widget=forms.TextInput(attrs={'type': 'text'}))

    class Meta:
        model = BikeServiceRequest
        fields = ['customer_name', 'phone_no', 'services', 'location', 'vehicle_model', 'license_plate_no', 'year']

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')
        if len(customer_name) < 4 or not customer_name.isalpha():
            raise ValidationError('Customer Name must be at least 4 letters and contain letters only.')
        return customer_name

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        validate_phone_number(phone_no)
        return phone_no

    def clean_license_plate_no(self):
        license_plate_no = self.cleaned_data.get('license_plate_no')
        validate_license_plate(license_plate_no)
        return license_plate_no

    

    def clean_year(self):
        year = self.cleaned_data.get('year')
        validate_year(year)
        return year
    
    def clean_vehicle_model(self):
        vehicle_model = self.cleaned_data.get('vehicle_model')
        validate_vehicle_model(vehicle_model)
        return vehicle_model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}),
    )
    address = forms.CharField(
        max_length=155,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Your address'}),
    )

    class Meta:
        model = Profile
        fields = ['phone_number', 'address']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address and len(address) < 10:
            raise ValidationError('Address must be at least 10 characters long.')
        return address

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 3 or not re.match("^[A-Za-z]*$", name):
            raise ValidationError('Name must contain only letters and be more than 3 characters long!')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            raise ValidationError('Invalid email format!')
        return email
