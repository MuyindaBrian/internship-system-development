from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Internship, InternshipApplication
from .serializers import InternshipSerializer, InternshipApplicationSerializer


class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def apply(self, request, pk=None):
        internship = self.get_object()
        application, created = InternshipApplication.objects.get_or_create(
            internship=internship,
            applicant=request.user
        )
        if created:
            return Response({'detail': 'Application submitted.'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Already applied.'}, status=status.HTTP_400_BAD_REQUEST)


class InternshipApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InternshipApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InternshipApplication.objects.filter(applicant=self.request.user)
