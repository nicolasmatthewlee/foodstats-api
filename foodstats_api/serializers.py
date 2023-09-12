from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "data_type",
            "description",
            "food_category_id",
            "publication_date",
        ]
