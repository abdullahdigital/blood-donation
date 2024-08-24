from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.email
    
# Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


# Donor Model
class Donor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    cnic = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=3)
    city = models.CharField(max_length=100)
    address = models.TextField()
    hospital = models.CharField(max_length=255, default='Unknown Hospital')
    has_notification = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.db import models
from uuid import uuid4

class BloodRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    hospital = models.CharField(max_length=255, default='Unknown Hospital')
    request_date = models.DateTimeField(auto_now_add=True)

from django.db import models
from uuid import uuid4
from django.conf import settings

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    BLOOD_REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    blood_request = models.ForeignKey(BloodRequest, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=BLOOD_REQUEST_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


# FAQ.py

from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
