from django.shortcuts import render

from . import views
from django.urls import path
from .views import dashboard, add_employee, login_view, custom_logout, submit_review, review_page, employee_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('base/',views.base, name='base'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile-saved/', views.profile_saved, name='profile_saved'),
    path('office-management/', views.office_management, name='office_management'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('book-appointment/', views.book_appointment, name='book-appointment'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('submit_review/', submit_review, name='submit_review'),
    path('review_page/', views.review_page, name='review_page'),
    path('add-meeting/', views.add_meeting, name='add_meeting'),
]