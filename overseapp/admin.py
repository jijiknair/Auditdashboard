from django.contrib import admin
# Register your models here.
from .models import UserProfile, MeetingRoom, Meeting, Task, ResourceRequest, Announcement, Appointment, \
    Employeenew

admin.site.register(UserProfile),
admin.site.register(Employeenew),
admin.site.register(MeetingRoom),
admin.site.register(Meeting),
admin.site.register(Task),
admin.site.register(ResourceRequest),
admin.site.register(Announcement),
admin.site.register(Appointment)