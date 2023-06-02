from django.urls import path
from .views import story_view

urlpatterns = [
    path('', story_view),
]