from django.urls import path
from .views import (
    ApiCitiesView,
    ApiDistrictsView,
    ApiListings,
    ApiListingsById,
)

urlpatterns = [
    path('cities', ApiCitiesView.as_view()),
    path('districts', ApiDistrictsView.as_view()),
    path('listings', ApiListings.as_view()),
    path('listings/<int:id>', ApiListingsById.as_view()),
]
