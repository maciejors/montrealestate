from django.urls import path
from .views import (
    ApiCitiesView,
    ApiDistrictsView,
)

urlpatterns = [
    path('cities', ApiCitiesView.as_view()),
    path('districts', ApiDistrictsView.as_view()),
]
