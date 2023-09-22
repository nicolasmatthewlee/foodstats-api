from rest_framework.views import APIView
from .models import Food, FoodCategory, Nutrient, FoodNutrient
from .serializers import (
    FoodSerializer,
    FoodCategorySerializer,
    NutrientSerializer,
    FoodNutrientSerializer,
)
from rest_framework.response import Response
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


class FoodCategoryList(APIView):
    """Lists food categories."""

    def get(self, request):
        categories = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(categories, many=True)
        return Response(serializer.data)


class NutrientList(APIView):
    """Lists nutrients."""

    def get(self, request):
        nutrients = Nutrient.objects.all()
        serializer = NutrientSerializer(nutrients, many=True)
        return Response(serializer.data)


class NutrientDetail(APIView):
    """Returns nutrient."""

    def get(self, request, pk):
        nutrient = get_object_or_404(Nutrient, pk=pk)
        serializer = NutrientSerializer(nutrient)
        return Response(serializer.data)


class FoodNutrientList(APIView):
    """Returns all nutrients for a specific food."""

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        nutrients = FoodNutrient.objects.filter(food=food)
        serializer = FoodNutrientSerializer(nutrients, many=True)
        return Response(serializer.data)
