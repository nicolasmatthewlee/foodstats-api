from rest_framework import serializers
from .models import Food, FoodCategory, Nutrient, FoodNutrient


class FoodSerializer(serializers.ModelSerializer):
    food_category = serializers.CharField(
        source="food_category.description", read_only=True
    )

    class Meta:
        model = Food
        fields = [
            "id",
            "data_type",
            "description",
            "food_category",
            "publication_date",
        ]


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["id", "description"]


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = "__all__"


class FoodNutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrient
        fields = "__all__"
