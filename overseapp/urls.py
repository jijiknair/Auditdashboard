from . import views
from django.urls import path

from django.urls import path
from .views import home, dashboard,register,available_offices,office_details

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('offices/', views.available_offices, name='available_offices'),
]