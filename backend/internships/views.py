from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Internship, InternshipApplication
from .serializers import InternshipSerializer, InternshipApplicationSerializer


class InternshipPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = InternshipPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'company', 'description']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        queryset = Internship.objects.all()
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

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
    pagination_class = InternshipPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['internship__title', 'internship__company']
    ordering_fields = ['applied_at', 'status']
    ordering = ['-applied_at']

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return InternshipApplication.objects.all()
        return InternshipApplication.objects.filter(applicant=user)
