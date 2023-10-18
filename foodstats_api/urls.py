"""foodstats_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    FoodList,
    FoodCategoryList,
    FoodDetail,
    NutrientList,
    NutrientDetail,
    FoodNutrientList,
    NutrientCategoryList,
)

urlpatterns = [
    path("api/foods/", FoodList.as_view()),
    path("api/foods/<int:pk>/", FoodDetail.as_view()),
    path("api/foods/<int:pk>/nutrients/", FoodNutrientList.as_view()),
    path("api/foods/categories/", FoodCategoryList.as_view()),
    path("api/nutrients/", NutrientList.as_view()),
    path("api/nutrients/categories/", NutrientCategoryList.as_view()),
    path("api/nutrients/<int:pk>/", NutrientDetail.as_view()),
]
