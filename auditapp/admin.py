from django.contrib import admin
from .models import FacilityAuditnewfinal, IPCProgram, AuditSummaryfinal, AuditResponsenewfinal, Opportunity
admin.site.register(FacilityAuditnewfinal)
admin.site.register(AuditResponsenewfinal)
admin.site.register(AuditSummaryfinal)
admin.site.register(Opportunity)
@admin.register(IPCProgram)
class IPCProgramAdmin(admin.ModelAdmin):
    list_display = ('ref_num', 'element', 'activity', 'scoring')
    search_fields = ('ref_num', 'element')
