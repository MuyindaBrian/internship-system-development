from rest_framework import serializers
from .models import MaintenanceRequest
from users.serializers import UserSerializer


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    requested_by = UserSerializer(read_only=True)

    class Meta:
        model = MaintenanceRequest
        fields = ['id', 'room', 'issue', 'status', 'requested_by', 'created_at', 'updated_at', 'resolved_at']
        read_only_fields = ['id', 'requested_by', 'created_at', 'updated_at', 'resolved_at']
        extra_kwargs = {
            'status': {'required': False}
        }
