from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class FoodList(APIView):
    """Lists foods with optional query parameter."""

    def get(self, request):
        # 1. if query provided, filter results
        query = request.GET.get("query")
        if query:
            foods = Food.objects.filter(description__icontains=query)
        else:
            foods = Food.objects.all()

        # 2. serialize and return results
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)


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
