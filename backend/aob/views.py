from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import AOBRequest
from .serializers import AOBRequestSerializer


class AOBRequestPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AOBRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AOBRequestSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AOBRequestPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return AOBRequest.objects.all()
        return AOBRequest.objects.filter(submitted_by=user)

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def approve(self, request, pk=None):
        aob_request = self.get_object()
        if request.user.user_type != 'admin':
            return Response({'detail': 'Only admins can approve requests.'}, status=status.HTTP_403_FORBIDDEN)

        if aob_request.status not in ('pending', 'in_review'):
            return Response({'detail': 'Cannot approve request in its current state.'}, status=status.HTTP_400_BAD_REQUEST)

        aob_request.status = 'approved'
        aob_request.reviewed_by = request.user
        aob_request.save()
        return Response({'detail': 'Request approved.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reject(self, request, pk=None):
        aob_request = self.get_object()
        if request.user.user_type != 'admin':
            return Response({'detail': 'Only admins can reject requests.'}, status=status.HTTP_403_FORBIDDEN)

        if aob_request.status not in ('pending', 'in_review'):
            return Response({'detail': 'Cannot reject request in its current state.'}, status=status.HTTP_400_BAD_REQUEST)

        response_text = request.data.get('response', '')
        aob_request.status = 'rejected'
        aob_request.reviewed_by = request.user
        aob_request.response = response_text
        aob_request.save()
        return Response({'detail': 'Request rejected.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def resolve(self, request, pk=None):
        aob_request = self.get_object()
        if request.user.user_type != 'admin':
            return Response({'detail': 'Only admins can resolve requests.'}, status=status.HTTP_403_FORBIDDEN)

        if aob_request.status != 'approved':
            return Response({'detail': 'Only approved requests can be resolved.'}, status=status.HTTP_400_BAD_REQUEST)

        from django.utils import timezone
        aob_request.status = 'resolved'
        aob_request.resolved_at = timezone.now()
        aob_request.save()
        return Response({'detail': 'Request resolved.'})
