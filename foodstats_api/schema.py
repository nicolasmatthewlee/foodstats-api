import graphene
from graphene_django import DjangoObjectType
from .models import Nutrient, FoodNutrient, Food, FoodCategory, NutrientCategory


class NutrientType(DjangoObjectType):
    class Meta:
        model = Nutrient
        fields = "__all__"


class FoodNutrientType(DjangoObjectType):
    class Meta:
        model = FoodNutrient
        fields = "__all__"


class FoodType(DjangoObjectType):
    class Meta:
        model = Food
        fields = "__all__"


class FoodCategoryType(DjangoObjectType):
    class Meta:
        model = FoodCategory
        fields = "__all__"


class NutrientCategoryType(DjangoObjectType):
    class Meta:
        model = NutrientCategory
        fields = "__all__"


class Query(graphene.ObjectType):
    nutrients = graphene.List(NutrientType)
    food_nutrients = graphene.List(FoodNutrientType)
    foods = graphene.List(FoodType)
    food_categories = graphene.List(FoodCategoryType)
    nutrient_categories = graphene.List(NutrientCategoryType)

    def resolve_nutrients(root, info):
        return Nutrient.objects.all()

    def resolve_food_nutrients(root, info):
        return FoodNutrient.objects.all()

    def resolve_foods(root, info):
        return Food.objects.all()

    def resolve_food_categories(root, info):
        return FoodCategory.objects.all()

    def resolve_nutrient_categories(root, info):
        return NutrientCategory.objects.all()


schema = graphene.Schema(query=Query)
