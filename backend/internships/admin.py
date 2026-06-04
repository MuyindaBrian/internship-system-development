from django.contrib import admin
from .models import Internship, InternshipApplication


class InternshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status', 'created_by', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'company', 'description']
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'internship', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['applicant__email', 'internship__title']
    readonly_fields = ['applied_at']


admin.site.register(Internship, InternshipAdmin)
admin.site.register(InternshipApplication, InternshipApplicationAdmin)
