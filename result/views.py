from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from result.serializers import SheetSerializer
from result.models import Sheet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND


class SheetViewset(viewsets.GenericViewSet):
        queryset = Sheet.objects.all()
        serializer_class = SheetSerializer

        def get_queryset(self): 
            queryset = Sheet.objects.all()
            return queryset

        @action(methods=['get'], detail=False)
        def filter(self, request, *args, **kwargs):
            q_param = self.request.query_params.get('query')
            queryset = None
            status = HTTP_404_NOT_FOUND
            if q_param:
                queryset = self.queryset.filter(Q(title__icontains=q_param) | Q(description_info__icontains=q_param))
                status = HTTP_200_OK
            serializer = SheetSerializer(queryset, many=True)
            
            return Response(serializer.data, status)

        # def update(self, request, *args, **kwargs):
        #     instance = self.ge