# -*- coding: utf-8 -*-
"""Module Docstring."""
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
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from wger.core.models import (
    UserProfile,
    Language,
    DaysOfWeek,
    License,
    RepetitionUnit,
    WeightUnit)


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to map to User model """
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])

    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:

        model = User
        fields = ('username', 'email', 'password')


class UserprofileSerializer(serializers.ModelSerializer):
    """Workout session serializer."""

    class Meta:
        """Class Docstring."""

        model = UserProfile


class UsernameSerializer(serializers.Serializer):
    """Serializer to extract the username."""

    username = serializers.CharField()


class LanguageSerializer(serializers.ModelSerializer):
    """Language serializer."""

    class Meta:
        """Class Docstring."""

        model = Language


class DaysOfWeekSerializer(serializers.ModelSerializer):
    """DaysOfWeek serializer."""

    class Meta:
        """Class Docstring."""

        model = DaysOfWeek


class LicenseSerializer(serializers.ModelSerializer):
    """License serializer."""

    class Meta:
        """Class Docstring."""

        model = License


class RepetitionUnitSerializer(serializers.ModelSerializer):
    """Repetition unit serializer."""

    class Meta:
        """Class Docstring."""

        model = RepetitionUnit


class WeightUnitSerializer(serializers.ModelSerializer):
    """Weight unit serializer."""

    class Meta:
        """Class Docstring."""

        model = WeightUnit
