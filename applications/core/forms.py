from django import forms

from applications.core import (
    conf as core_conf,
    strings as core_strings,
    models as core_models,
)


class Board(forms.ModelForm):
    class Meta:
        model = core_models.Board
        fields = (
            'name',
            'is_private'
        )
        labels = {
            'name': core_strings.BOARD_NAME_LABEL,
            'is_private': core_strings.BOARD_PRIVATE_LABEL,
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'is_private': forms.CheckboxInput(attrs={"class": "form-control"}),
        }
