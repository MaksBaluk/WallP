from django.urls import path
from .views import WallTemplate

urlpatterns = [
    path('', WallTemplate.as_view(),name='main'),
]
