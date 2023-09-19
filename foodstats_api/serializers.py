from rest_framework import serializers
from .models import Food, FoodCategory


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
