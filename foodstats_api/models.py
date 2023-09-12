from django.db import models


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
    food_category_id = models.IntegerField()
    publication_date = models.DateField()


class FoodNutrient(models.Model):
    """The amount of a nutrient in a specific food."""

    food_id = models.ForeignKey("Food", on_delete=models.CASCADE)
    nutrient_id = models.IntegerField()
    amount = models.FloatField()
    data_points = models.IntegerField()
    derivation_id = models.IntegerField()
    min = models.FloatField()
    max = models.FloatField()
    median = models.FloatField()
    footnote = models.CharField(max_length=15)
    min_year_acquired = models.IntegerField()
    pass


class Nutrient(models.Model):
    """A type of nutrient."""

    name = models.CharField(max_length=70)
    unit_name = models.CharField(max_length=10)
