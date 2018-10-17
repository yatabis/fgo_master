from django.urls import path

from .views import TopMenuView
from .views import CardDataView, SynthesisSchemeView, BattleSimulatorView
from .views import ServantView, CraftEssenceView, CommandCodeView, MysticCodeView
from .views import ServantDetailView

urlpatterns = [
    path('top-menu/', TopMenuView.as_view(), name="top-menu"),

    path('card-data/', CardDataView.as_view(), name="card-data"),
    path('synthesis-scheme/', SynthesisSchemeView.as_view(), name="synthesis-scheme"),
    path('battle-simulator', BattleSimulatorView.as_view(), name="battle-simulator"),

    path('card-data/servant/', ServantView.as_view(), name="servant"),
    path('card-data/craft-essence/', CraftEssenceView.as_view(), name="craft-essence"),
    path('card-data/command-code/', CommandCodeView.as_view(), name="command-code"),
    path('card-data/mystic-code/', MysticCodeView.as_view(), name="mystic-code"),

    path('card-data/servant/<str:name>/', ServantDetailView.as_view(), name="servant-detail"),
]
