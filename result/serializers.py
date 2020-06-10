from result.models import Sheet
# Create your views here.
from rest_framework import serializers

class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'