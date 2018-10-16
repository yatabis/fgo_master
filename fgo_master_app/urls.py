from django.urls import path

from .views import TopMenuView
from .views import CardDataView, SynthesisSchemeView, BattleSimulatorView

urlpatterns = [
    path('top-menu/', TopMenuView.as_view(), name="top-menu"),
    path('card-data/', CardDataView.as_view(), name="card-data"),
    path('synthesis-scheme/', SynthesisSchemeView.as_view(), name="synthesis-scheme"),
    path('battle-simulator', BattleSimulatorView.as_view(), name="battle-simulator")
]
