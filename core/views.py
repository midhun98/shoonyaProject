from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import RetreatsFilter
from .models import Retreat
from .serializers import RetreatSerializer


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RetreatViewSet(viewsets.ModelViewSet):
    queryset = Retreat.objects.all().order_by('id')
    pagination_class = CustomPageNumberPagination
    serializer_class = RetreatSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RetreatsFilter
    search_fields = ['title', 'location', 'description']
    ordering_fields = ['price', 'duration']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
