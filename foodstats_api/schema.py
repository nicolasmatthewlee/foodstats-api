import graphene
from graphene_django import DjangoObjectType
from .models import Nutrient


class NutrientType(DjangoObjectType):
    class Meta:
        model = Nutrient
        fields = ("id", "name")


class Query(graphene.ObjectType):
    nutrients = graphene.List(NutrientType)

    def resolve_nutrients(root, info):
        return Nutrient.objects.all()


schema = graphene.Schema(query=Query)
