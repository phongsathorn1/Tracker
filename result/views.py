from django.db.models import Q
from rest_framework import viewsets, mixins
from result.serializers import SheetSerializer
from result.models import Sheet
from rest_framework.response import Response


class SheetViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
        queryset = Sheet.objects.all()
        serializer_class = SheetSerializer

        def list(self, request, *args, **kwargs):
            q_param = self.request.query_params.get('query')
            queryset = self.queryset.filter(Q(Title__icontains=q_param) | Q(Body__icontains=q_param))
            serializer = SheetSerializer(queryset, many=True)
            return Response(serializer.data)

