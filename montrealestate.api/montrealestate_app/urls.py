from django.urls import path
from .views import (
    ApiCitiesView,
    ApiDistrictsView,
    ApiCategoriesView,
)

urlpatterns = [
    path('cities', ApiCitiesView.as_view()),
    path('districts', ApiDistrictsView.as_view()),
    path('categories', ApiCategoriesView.as_view()),
]
