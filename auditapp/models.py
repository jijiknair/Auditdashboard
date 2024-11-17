from django.db import models
from django.contrib.auth.models import User

class FacilityAuditnewfinal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility_name = models.CharField(max_length=255)
    governate = models.CharField(max_length=100)
    wilayat = models.CharField(max_length=100)
    head_of_institution = models.CharField(max_length=255)
    rationale = models.CharField(max_length=100)
    audit_date = models.DateField()
    lead_auditor = models.CharField(max_length=255)
    auditors = models.TextField()
    areas_covered = models.TextField()

    def __str__(self):
        return self.facility_name

class AuditResponsenewfinal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with a user
    page_number = models.IntegerField()
    ref_no = models.CharField(max_length=10)
    description = models.TextField()
    response = models.CharField(max_length=20, choices=[('Met', 'Met'), ('Partially Met', 'Partially Met'), ('Not Met', 'Not Met')])
    audit_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Page {self.page_number}, Element {self.ref_no}: {self.response}"


class AuditSummaryfinal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    met_count = models.IntegerField(default=0)  # Count of "Met"
    partially_met_count = models.IntegerField(default=0)  # Count of "Partially Met"
    not_met_count = models.IntegerField(default=0)  # Count of "Not Met"
    comments = models.TextField(blank=True, null=True)  # User comments for the page
    photo = models.ImageField(upload_to='audit_photos/', blank=True, null=True)  # Upload photos (optional)
    def __str__(self):
        return self.heading


class IPCProgram(models.Model):
    ref_num = models.CharField(max_length=10)
    element = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    scoring_options = [
        ('NA', 'Not Applicable'),
        ('Met', 'Met'),
        ('Partially Met', 'Partially Met'),
        ('Not Met', 'Not Met'),
    ]
    scoring = models.CharField(max_length=20, choices=scoring_options)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ref_num}: {self.element}"

class Opportunity(models.Model):
    opp_number = models.IntegerField(default=1)  # Start from 1 or any initial value
    def __str__(self):
        return f"Opportunity {self.opp_number}"


class Indication(models.Model):
    session_no = models.IntegerField()
    opp_hr = models.IntegerField(default=0)  # Opportunities for hand rub
    act_hr = models.IntegerField(default=0)  # Actions for hand rub
    opp_hw = models.IntegerField(default=0)  # Opportunities for hand wash
    act_hw = models.IntegerField(default=0)  # Actions for hand wash
    # Additional fields for other categories as needed
    def __str__(self):
        return f"Session {self.session_no}"