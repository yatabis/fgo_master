from django.urls import path

from .views import TopMenuView

urlpatterns = [
    path('top-menu/', TopMenuView.as_view(), name="top-menu")
]
