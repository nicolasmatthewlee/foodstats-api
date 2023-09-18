from rest_framework import serializers
from .models import Food


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
