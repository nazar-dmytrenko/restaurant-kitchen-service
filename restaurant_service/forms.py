from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Cook


from restaurant_service.models import Dish, DishType
import re


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )


class CookCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "*Username: ",
                "class": "form-control"
            }
        ),
        label=""
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name: ",
                "class": "form-control"

            }
        ),
        label=""
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name: ",
                "class": "form-control"

            }
        ),
        label=""
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ),
        label=""
    )
    years_of_experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Years of experience:",
                "class": "form-control"

            }
        ),
        label=""
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ),
        label=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ),
        label=""
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
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "*Username: ",
                "class": "form-control"
            }
        ),
        label=""
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name: ",
                "class": "form-control"

            }
        ),
        label=""
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name: ",
                "class": "form-control"

            }
        ),
        label=""
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ),
        label=""
    )
    years_of_experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Years of experience:",
                "class": "form-control"

            }
        ),
        label=""
    )

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "first_name", "last_name")


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search the dish by username..."}
        )
    )


class DishForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name: ",
                "class": "form-control"
            }

        ),
        label="")
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description: ",
                "class": "form-control"
            }
        ),
        label="")
    price = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Price:",
                "class": "form-control"
            }
        ),
        label=""
    )
    dish_type = forms.ModelChoiceField(
        queryset=DishType.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Choose the dish type",
                "class": "form-control"
            }
        ),
        label=""
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.filter(is_superuser=False, is_staff=False),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search the dish by name..."}
        )
    )


class DishTypeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "*Name",
                "class": "form-control"
            }

        )
    )

    class Meta:
        model = DishType
        fields = "__all__"

    def clean_name(self):
        pattern = r"^[a-zA-Z\s]+$"
        name = self.cleaned_data["name"]
        if not re.match(pattern, name):
            raise ValidationError("Name can't contain digits!")
        return name


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search the dish by name..."}
        )
    )

