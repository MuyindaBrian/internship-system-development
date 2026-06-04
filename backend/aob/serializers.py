from rest_framework import serializers
from .models import AOBRequest
from users.serializers import UserSerializer


class AOBRequestSerializer(serializers.ModelSerializer):
    submitted_by = UserSerializer(read_only=True)
    reviewed_by = UserSerializer(read_only=True)

    class Meta:
        model = AOBRequest
        fields = ['id', 'title', 'description', 'category', 'status', 'submitted_by', 'reviewed_by', 'response', 'created_at', 'updated_at', 'resolved_at']
        read_only_fields = ['id', 'submitted_by', 'reviewed_by', 'created_at', 'updated_at', 'resolved_at']
