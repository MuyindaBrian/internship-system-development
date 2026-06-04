from django.db import models
from users.models import CustomUser


class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    room = models.CharField(max_length=100)
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='maintenance_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Room {self.room} - {self.issue[:50]}"

    class Meta:
        db_table = 'maintenance_requests'
        ordering = ['-created_at']
