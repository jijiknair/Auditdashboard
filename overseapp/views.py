# views.py
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile, AnalyticsData, Employeenew
from django.shortcuts import render, redirect
from .forms import AppointmentForm, SignUpForm, MeetingForm
from .models import Meeting, Task, ResourceRequest, Announcement
from .forms import EmployeeForm
from django.contrib.auth import login as auth_login, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def edit_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile_image = request.FILES.get('image')

        # Get the current user
        user = request.user

        # Check if profile exists and update or create it
        user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={
            'name': name,
            'email': email,
            'profile_image': profile_image
        })

        if not created:
            user_profile.name = name
            user_profile.email = email
            if profile_image:
                user_profile.profile_image = profile_image
            user_profile.save()

        return redirect('profile_saved')  # Redirect to a success page after saving

    return render(request, 'base.html')

def profile_saved(request):
    return render(request, 'profile_saved.html')

def office_management(request):
    employees = Employeenew.objects.all()
    meetings = Meeting.objects.all()
    tasks = Task.objects.filter(assigned_to=request.user)
    requests = ResourceRequest.objects.filter(requested_by=request.user)
    announcements = Announcement.objects.all()

    return render(request, 'office_management.html', {
        'employees': employees,
        'meetings': meetings,
        'tasks': tasks,
        'requests': requests,
        'announcements': announcements,
    })



def dashboard(request):
    return render(request,'login.html')

def base(request):
    return render(request,'base.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def office_managementnew(request):
    employees = Employeenew.objects.all()  # Get all employees from the new model
    return render(request, 'office_management.html', {'employees': employees})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointment_success')  # Redirect to a success page or any other page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()

    return render(request, 'book-appointment.html', {'form': form})

def analytics_dashboard(request):
    # Fetching data from the AnalyticsData model
    analytics_data = AnalyticsData.objects.all()
    # Prepare data for Chart.js
    page_names = [data.page_name for data in analytics_data]
    page_views = [data.views for data in analytics_data]
    unique_users = [data.unique_users for data in analytics_data]
    avg_time_spent = [data.avg_time_spent for data in analytics_data]

    context = {
        'page_names': page_names,
        'page_views': page_views,
        'unique_users': unique_users,
        'avg_time_spent': avg_time_spent,
    }

    return render(request, 'analytics_dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')  # Change 'dashboard' to your desired redirect
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirmpassword = form.cleaned_data.get('confirmpassword')

            # Ensure the passwords match
            if password == confirmpassword:
                # Create the user
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Your account has been created successfully!')
                return redirect('login')  # Redirect to login page
            else:
                messages.error(request, 'Passwords do not match')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def submit_review(request):
    if request.method == 'POST':
        messages.success(request, 'Your review has been submitted successfully!')
        return redirect('review_page')  # Redirect to review_page after submission
    else:
        return render(request, 'base.html')  # Handle GET requests if necessary

def review_page(request):
    return render(request, 'review.html')  # Render the review.html page

def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.booked_by = request.user  # Assign the logged-in user to the booked_by field
            meeting.save()
            return redirect('office_management')  # Redirect to your meetings page after adding
    else:
        form = MeetingForm()

    return render(request, 'add_meeting.html', {'form': form})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_management')  # Redirect to the list of employees after saving
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})