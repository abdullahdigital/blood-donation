# views.py

from django.shortcuts import render
from .models import FAQ
from .forms import ContactForm

def home(request):
    success_message = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Your message has been successfully submitted. We will get back to you shortly."
            form = ContactForm()  # Reset the form after successful submission
    else:
        form = ContactForm()

    # Retrieve all FAQ items from the database
    faqs = FAQ.objects.all()

    context = {
        'form': form,
        'success_message': success_message,
        'faqs': faqs,  # Pass the FAQs to the context
    }
    return render(request, 'donation/home.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            elif CustomUser.objects.filter(phone=phone).exists():
                messages.error(request, 'Phone number already exists')
            else:
                hashed_password = make_password(password1)
                user = CustomUser(
                    username=username,
                    email=email,
                    phone=phone,
                    password=hashed_password  # Set hashed password
                )
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'donation/signup.html') 



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # Create a form to handle email and password inputs

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()

    return render(request, 'donation/login.html', {'form': form})
#logout
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout



def about(request):
    return render(request, 'donation/about.html')




                        #Volunteer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Donor
from .forms import DonorForm

@login_required
def volunteer_view(request):
    try:
        donor = Donor.objects.get(user=request.user)
    except Donor.DoesNotExist:
        donor = None

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            return redirect('home')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'donation/volunteer.html', {'form': form})




                        # Request blood
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BloodRequest, Notification, Donor
from django.contrib import messages

@login_required
def request_blood_view(request):
    if request.method == 'POST':
        blood_type = request.POST['blood_type']
        city = request.POST['city']
        address = request.POST['address']
        phone = request.POST['phone']
        hospital = request.POST['hospital']

        blood_request = BloodRequest.objects.create(
            user=request.user,
            blood_type=blood_type,
            city=city,
            address=address,
            phone=phone,
            hospital=hospital
        )

        # Find matching donors
        donors = Donor.objects.filter(blood_type=blood_type)

        for donor in donors:
            Notification.objects.create(
                blood_request=blood_request,
                donor=donor  # Associate notification with the donor
            )

        messages.success(request, 'Your blood request has been submitted.')
        return redirect('notifications')

    return render(request, 'donation/request_blood.html')


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Add this import
from .models import Notification, BloodRequest, Donor
import json

@login_required
def notifications_view(request):
    user = request.user
    # Get all notifications where the user is either the donor or the receiver of the blood request
    notifications = Notification.objects.filter(
        Q(donor__user=user) | Q(blood_request__user=user)
    ).order_by('-created_at')

    return render(request, 'donation/notifications.html', {'notifications': notifications})

@login_required
def update_notification_status(request, notification_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_status = data.get('status')
        
        notification = get_object_or_404(Notification, id=notification_id)
        notification.status = new_status
        notification.save()
        
        response_data = {'success': True, 'blood_request_id': notification.blood_request.id}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)





from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_count(request):
    try:
        donor = request.user.donor
        count = Notification.objects.filter(donor=donor, status='pending').count()
    except Donor.DoesNotExist:
        count = 0

    return JsonResponse({'count': count})


from django.shortcuts import render, get_object_or_404
from .models import BloodRequest, Notification

def request_blood_success(request, request_id):
    # Get the blood request
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    
    # Try to find a notification related to this blood request with an approved status
    notification = Notification.objects.filter(blood_request=blood_request, status='approved').first()
    
    if notification and notification.donor:
        # Donor found
        donor = notification.donor
        return render(request, 'donation/blood_request_success.html', {'donor': donor})
    else:
        # No donor found
        return render(request, 'donation/blood_request_success.html', {
            'error_message': 'Donor details not found.'
        })








