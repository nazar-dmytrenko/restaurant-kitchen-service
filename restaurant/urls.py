"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from restaurant_service.views import (
    index_view,

    DishListView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
    DishDeleteView,

    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishUpdateCookView,

    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    login_view,
    register_user
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="home"),
    path("login/",  login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("create_dish/", DishCreateView.as_view(), name="create_dish"),
    path("dishtypes/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cook-page/<int:pk>", CookDetailView.as_view(), name="cook-page"),
    path("dish-page/<int:pk>", DishDetailView.as_view(), name="dish-page"),
    path("dishtype-page/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-page"),
    path("cook/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dishtype/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.MEDIA_URL_1, document_root=settings.MEDIA_ROOT_1)

