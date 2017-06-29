# -*- coding: utf-8 -*-
"""Docstring."""
from __future__ import unicode_literals

from django.db import models, migrations  # noqa
from sortedm2m.operations import AlterSortedManyToManyField
import sortedm2m.fields


class Migration(migrations.Migration):
    """Docstring."""

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='set',
            name='exercises',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None,
                                                         to='exercises.Exercise',
                                                         verbose_name='Exercises'),
            preserve_default=True,
        )
    ]
