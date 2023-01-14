from django.urls import path
from .views import (
    ApiListings,
    ApiListingsById,
)

urlpatterns = [
    path('', ApiListings.as_view()),
    path('<int:id>', ApiListingsById.as_view()),
]
