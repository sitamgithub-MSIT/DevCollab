from django.urls import path
from . import views


urlpatterns = [

    path('' , views.getroutes),
    path('rooms/', views.getrooms),
    path('rooms/<str:pk>/', views.getroom),

]