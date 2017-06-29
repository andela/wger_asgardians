# -*- coding: utf-8 -*-
"""This file contains forms used in the application."""
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


from captcha.fields import ReCaptchaField

from django.utils.translation import ugettext as _
from django.forms import (
    Form,
    MultipleHiddenInput,
    ModelForm,
    DateField,
    IntegerField,
    DecimalField,
    CharField,
    widgets,
    ModelChoiceField
)

from wger.core.models import (
    RepetitionUnit,
    WeightUnit
)
from wger.exercises.models import (
    Exercise,
    ExerciseCategory
)
from wger.manager.models import (
    WorkoutSession,
    Workout,
    Day,
    Set,
    Setting,
    WorkoutLog
)
from wger.utils.widgets import (
    TranslatedSelectMultiple,
    TranslatedSelect,
    ExerciseAjaxSelect
)
from wger.utils.constants import DATE_FORMATS
from wger.utils.widgets import Html5DateInput


class DemoUserForm(Form):
    """Docstring."""

    captcha = ReCaptchaField(attrs={'theme': 'clean'},
                             label=_('Confirmation text'),
                             help_text=_('As a security measure, please enter the previous words'),)


class WorkoutForm(ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Workout
        exclude = ('user',)


class WorkoutCopyForm(Form):
    """Docstring."""

    comment = CharField(max_length=100,
                        help_text=_('The goal or description of the new workout.'),
                        required=False)


class DayForm(ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Day
        exclude = ('training',)
        widgets = {'day': TranslatedSelectMultiple()}


class SetForm(ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Set
        exclude = ('order', 'exerciseday')
        widgets = {'exercises': ExerciseAjaxSelect(), }

    # We need to overwrite the init method here because otherwise Django
    # will output a default help text, regardless of the widget used
    # https://code.djangoproject.com/ticket/9321
    def __init__(self, *args, **kwargs):
        """Docstring."""
        super(SetForm, self).__init__(*args, **kwargs)
        self.fields['exercises'].help_text = _('You can search for more than one exercise, '
                                               'they will be grouped together for a superset.')


class SetFormMobile(ModelForm):
    """Don't use the auto completer when accessing the mobile version."""

    class Meta:
        """Docstring."""

        model = Set
        exclude = ('order', 'exerciseday')
        widgets = {'exercises': MultipleHiddenInput(), }

    categories_list = ModelChoiceField(ExerciseCategory.objects.all(),
                                       empty_label=_('All categories'),
                                       label=_('Categories'),
                                       widget=TranslatedSelect(),
                                       required=False)
    exercise_list = ModelChoiceField(Exercise.objects)

    # We need to overwrite the init method here because otherwise Django
    # will output a default help text, regardless of the widget used
    # https://code.djangoproject.com/ticket/9321
    def __init__(self, *args, **kwargs):
        """Docstring."""
        super(SetFormMobile, self).__init__(*args, **kwargs)
        self.fields['exercise_list'].help_text = _('You can search for more than one exercise, '
                                                   'they will be grouped together for a superset.')


class SettingForm(ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Setting
        exclude = ('set', 'exercise', 'order', 'comment')


class HelperDateForm(Form):
    """A helper form used in the workout log view."""

    date = DateField(input_formats=DATE_FORMATS, widget=Html5DateInput())


class WorkoutLogForm(ModelForm):
    """Helper form for a WorkoutLog.

    These fields are re-defined here only to make them optional

    """

    repetition_unit = ModelChoiceField(queryset=RepetitionUnit.objects.all(),
                                       label=_('Unit'),
                                       required=False)
    weight_unit = ModelChoiceField(queryset=WeightUnit.objects.all(),
                                   label=_('Unit'),
                                   required=False)
    exercise = ModelChoiceField(queryset=Exercise.objects.all(),
                                label=_('Exercise'),
                                required=False)
    reps = IntegerField(label=_('Repetitions'),
                        required=False)
    weight = DecimalField(label=_('Weight'),
                          initial=0,
                          required=False)

    class Meta:
        """Docstring."""

        model = WorkoutLog
        exclude = ('workout', )


class HelperWorkoutSessionForm(ModelForm):
    """A helper form used in the workout log view."""

    class Meta:
        """Docstring."""

        model = WorkoutSession
        exclude = ('user', 'workout', 'date')


class WorkoutSessionForm(ModelForm):
    """Workout Session form."""

    class Meta:
        """Docstring."""

        model = WorkoutSession
        exclude = ('user', 'workout', 'date')


class WorkoutSessionHiddenFieldsForm(ModelForm):
    """Workout Session form used in the timer view."""

    class Meta:
        """Docstring."""

        model = WorkoutSession
        exclude = []
        widgets = {'time_start': widgets.HiddenInput(),
                   'time_end': widgets.HiddenInput(),
                   'user': widgets.HiddenInput(),
                   'notes': widgets.Textarea(attrs={'rows': 3})}
