from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer


class FoodList(ListAPIView):
    """Provides default list and retrieve actions."""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
