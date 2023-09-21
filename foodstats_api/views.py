from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class FoodList(ListAPIView):
    """Lists foods."""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(APIView):
    """Returns individual food."""

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)


class FoodCategoryList(ListAPIView):
    """Lists food categories."""

    pagination_class = None
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
