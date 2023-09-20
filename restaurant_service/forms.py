from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from restaurant_service.models import Dish, DishType
import re


class CookCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "*Username: "}
        ),
        label=""
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "First_name: "}
        ),
        label=""
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Last name: "}
        ),
        label=""
    )
    years_of_experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "*Years of experience:"}
        ),
        label= ""
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "years_of_experience"
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if years_of_experience < 0:
            raise ValidationError("Experience can't be a negative number!")
        if years_of_experience > 60:
            raise ValidationError("Cook can't have that much of experience!")
        return years_of_experience


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "years_of_experience", "first_name", "last_name"]