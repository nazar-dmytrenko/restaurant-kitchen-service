from django.contrib.auth import get_user_model, login, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic


from restaurant_service.forms import (
    CookCreationForm,
    CookSearchForm,
    CookUpdateForm,
    DishForm,
    DishSearchForm,
    DishTypeForm,
    DishTypeSearchForm
)
from restaurant_service.models import (Cook, Dish, DishType)
