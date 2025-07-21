from django.urls import path
from .views import get_reviews_by_section

urlpatterns = [
    path('api/reviews/', get_reviews_by_section, name='get_reviews_by_section'),
]
