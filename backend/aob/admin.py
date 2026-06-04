from django.contrib import admin
from .models import AOBRequest


class AOBRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'submitted_by', 'reviewed_by', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'description', 'submitted_by__email']
    readonly_fields = ['submitted_by', 'created_at', 'updated_at', 'resolved_at']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.submitted_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(AOBRequest, AOBRequestAdmin)
