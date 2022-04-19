from rest_framework.serializers import ModelSerializer

from .models import SalesOrder


class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount','description']