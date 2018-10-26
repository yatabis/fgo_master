from django.urls import path

from .views import TopMenuView
from .views import SpiritOriginView, SynthesisSchemeView, BattleSimulatorView
from .views import ServantView, CraftEssenceView, CommandCodeView, MysticCodeView
from .views import ServantDetailView

urlpatterns = [
    path('', TopMenuView.as_view(), name="top-menu"),

    path('spirit-origin/', SpiritOriginView.as_view(), name="spirit-origin"),
    path('synthesis-scheme/', SynthesisSchemeView.as_view(), name="synthesis-scheme"),
    path('battle-simulator', BattleSimulatorView.as_view(), name="battle-simulator"),

    path('spirit-origin/servant/', ServantView.as_view(), name="servant"),
    path('spirit-origin/craft-essence/', CraftEssenceView.as_view(), name="craft-essence"),
    path('spirit-origin/command-code/', CommandCodeView.as_view(), name="command-code"),
    path('spirit-origin/mystic-code/', MysticCodeView.as_view(), name="mystic-code"),

    path('spirit-origin/servant/<str:name><int:pk>/', ServantDetailView.as_view(), name="servant-detail"),
]
