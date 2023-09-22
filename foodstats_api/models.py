from django.db import models


class FoodCategory(models.Model):
    """A food category."""

    description = models.CharField(max_length=35)


class Food(models.Model):
    """A food instance."""

    DATA_TYPES = [
        ("sample_food", "sample_food"),
        ("market_acquisition", "market_acquisition"),
        ("sub_sample_food", "sub_sample_food"),
        ("foundation_food", "foundation_food"),
        ("agricultural_acquisition", "agricultural_acquisition"),
    ]

    data_type = models.CharField(max_length=30, choices=DATA_TYPES)
    description = models.CharField(max_length=150)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    publication_date = models.DateField()


class FoodNutrient(models.Model):
    """The amount of a nutrient in a specific food."""

    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    nutrient = models.ForeignKey("Nutrient", on_delete=models.CASCADE)
    amount = models.FloatField()
    data_points = models.IntegerField()
    derivation_id = models.IntegerField()
    min = models.FloatField(null=True)
    max = models.FloatField(null=True)
    median = models.FloatField(null=True)
    footnote = models.CharField(max_length=15, null=True)
    min_year_acquired = models.IntegerField(null=True)
    pass


class Nutrient(models.Model):
    """A type of nutrient."""

    name = models.CharField(max_length=70)
    unit_name = models.CharField(max_length=10)
