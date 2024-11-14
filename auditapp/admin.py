from django.contrib import admin
from .models import FacilityAuditnew, IPCProgram, AuditSummary, AuditResponsenew, Opportunity

admin.site.register(FacilityAuditnew)
admin.site.register(AuditResponsenew)
admin.site.register(AuditSummary)
admin.site.register(Opportunity)
@admin.register(IPCProgram)
class IPCProgramAdmin(admin.ModelAdmin):
    list_display = ('ref_num', 'element', 'activity', 'scoring')
    search_fields = ('ref_num', 'element')
