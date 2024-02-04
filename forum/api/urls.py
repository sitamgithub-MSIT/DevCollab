from django.urls import path
from . import views

"""
This module defines the URL patterns for the forum API.

- The path '' maps to the getroutes view function.
- The path 'rooms/' maps to the getrooms view function.
- The path 'rooms/<str:pk>/' maps to the getroom view function.
"""

urlpatterns = [
    path("", views.getroutes),
    path("rooms/", views.getrooms),
    path("rooms/<str:pk>/", views.getroom),
]
