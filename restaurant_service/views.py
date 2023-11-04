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


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, "")  #restaurant/index.html


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.prefetch_related("cooks")


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "" #restaurant/dish_form.html


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "" #restaurant/dish_form.html


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "" #restaurant/dish_confirm_delete.html


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeDetailView(generic.DetailView):
    template_name = "" #restaurant/dish_type_detail.html
    context_object_name = "dish_type"
    model = DishType
    queryset = DishType.objects.all()


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    context_object_name = "dish_type"
    template_name = "" #restaurant/dish_type_form.html


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    context_object_name = "dish_type"
    form_class = DishTypeForm
    template_name = "" #restaurant/dish_type_form.html


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    context_object_name = "dish_type"
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "" #restaurant/dish_type_confirm_delete.html

