from rest_framework import serializers
from .models import Internship, InternshipApplication
from users.serializers import UserSerializer


class InternshipSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Internship
        fields = ['id', 'title', 'description', 'company', 'duration', 'status', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']


class InternshipApplicationSerializer(serializers.ModelSerializer):
    internship = InternshipSerializer(read_only=True)
    applicant = UserSerializer(read_only=True)

    class Meta:
        model = InternshipApplication
        fields = ['id', 'internship', 'applicant', 'status', 'applied_at']
        read_only_fields = ['id', 'applicant', 'applied_at']
