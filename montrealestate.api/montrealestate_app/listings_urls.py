from django.urls import path
from .views import (
    ApiListings
)

urlpatterns = [
    path('', ApiListings.as_view()),
]
