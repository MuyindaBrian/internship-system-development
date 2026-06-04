from django.contrib import admin
from .models import MaintenanceRequest


class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'status', 'requested_by', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['room', 'issue', 'requested_by__email']
    readonly_fields = ['requested_by', 'created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.requested_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)
