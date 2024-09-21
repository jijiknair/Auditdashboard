from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
# profile/models.py
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    def __str__(self):
        return self.user.username


    # Meeting Room Booking model
class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Meeting(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # Task Assignment model
class Task(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # Resource Request model
class ResourceRequest(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=100)  # e.g., 'Laptop', 'Projector'
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')

    # Announcement model
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

class Appointment(models.Model):
    office_name = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f"{self.office_name} - {self.office_location} on {self.date} at {self.time}"

# models.py
class AnalyticsData(models.Model):
    page_name = models.CharField(max_length=100)
    views = models.IntegerField()
    unique_users = models.IntegerField()
    avg_time_spent = models.FloatField()  # Average time spent in seconds

    def __str__(self):
        return self.page_name

def review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        messages.success(request, 'Your review has been successfully submitted!')
        return redirect('review_success')  # Redirect to a success page
    return HttpResponse('Invalid request method', status=400)


class Employeenew(models.Model):
    name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100, blank=True)  # Add job position field
    def __str__(self):
        return f"{self.name} - {self.job_position}"

