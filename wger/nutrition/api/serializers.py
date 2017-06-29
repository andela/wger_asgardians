# -*- coding: utf-8 -*-
"""Docstring."""

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework import serializers
from wger.nutrition.models import (
    NutritionPlan,
    IngredientWeightUnit,
    WeightUnit,
    MealItem,
    Meal,
    Ingredient
)


class NutritionPlanSerializer(serializers.ModelSerializer):
    """Nutritional plan serializer."""

    class Meta:
        """Docstring."""

        model = NutritionPlan
        exclude = ('user',)


class IngredientWeightUnitSerializer(serializers.ModelSerializer):
    """IngredientWeightUnit serializer."""

    class Meta:
        """Docstring."""

        model = IngredientWeightUnit


class WeightUnitSerializer(serializers.ModelSerializer):
    """WeightUnit serializer."""

    class Meta:
        """Docstring."""

        model = WeightUnit


class MealItemSerializer(serializers.ModelSerializer):
    """MealItem serializer."""

    meal = serializers.PrimaryKeyRelatedField(label='Nutrition plan',
                                              queryset=Meal.objects.all())

    class Meta:
        """Docstring."""

        model = MealItem


class MealSerializer(serializers.ModelSerializer):
    """Meal serializer."""

    plan = serializers.PrimaryKeyRelatedField(label='Nutrition plan',
                                              queryset=NutritionPlan.objects.all())

    class Meta:
        """Docstring."""

        model = Meal


class IngredientSerializer(serializers.ModelSerializer):
    """Ingredient serializer."""

    class Meta:
        """Docstring."""

        model = Ingredient
