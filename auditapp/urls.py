from django.shortcuts import render
from . import views
from django.urls import path
from .views import dashboard, login_view, custom_logout, audit_form_view, facility_view, ipc_audit_healthcare, \
    basefrm, ipc_audit_page, signup_view

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('base/',views.base, name='base'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('audit-form/', audit_form_view, name='audit_form'),
    path('facility/', facility_view, name='facility'),
    path('explanation/', views.explanation_view, name='explanation_page'),
    path('ipc_audit_healthcare/', ipc_audit_healthcare, name='ipc_audit_healthcare'),
    path('basefrm/', basefrm, name='basefrm'),
    path('audit_summary/', views.audit_summary, name='audit_summary'),
    path('ipc_audit/<int:page_number>/', views.ipc_audit_page, name='ipc_audit_page'),
    path('audit-selection/', views.audit_selection, name='audit_selection'),
    path('endoscopy_audit/', views.endoscopy_audit, name='endoscopy_audit'),
    path('facility-endoscopy/', views.facility_endoscopy, name='facilityendos'),
    path('explanation2/', views.explanation2_view, name='explanation2'),
    path('handhygienenew/', views.handhygienenew, name='handhygienenew'),
    path('general_instruction/',views.general_instruction, name='general_instruction'),
    path('profcat/',views.profcat, name='profcat'),
    path('opportunities/',views.opportunities, name='opportunities'),
    path('formselection/', views.formselection, name='formselection'),
    path('new-opportunity/', views.new_opportunity, name='new_opportunity'),
    path('hhactionform/', views.hhactionform, name='hhactionform'),
    path('compliance_chart/', views.compliance_chart, name='compliance_chart'),
    ]