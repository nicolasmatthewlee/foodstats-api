from rest_framework.generics import ListAPIView
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodCategorySerializer


class FoodList(ListAPIView):
    """Lists foods."""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodCategoryList(ListAPIView):
    """Lists food categories."""

    pagination_class = None
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
