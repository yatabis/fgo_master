from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Servant

# Create your views here.


# ルート階層
class TopMenuView(TemplateView):
    template_name = "fgo_master_app/top-menu.html"


# TopMenu階層
class CardDataView(TemplateView):
    template_name = "fgo_master_app/card-data.html"


class SynthesisSchemeView(TemplateView):
    template_name = "fgo_master_app/synthesis-scheme.html"


class BattleSimulatorView(TemplateView):
    template_name = "fgo_master_app/battle-simulation.html"


# CardData階層
class ServantView(ListView):
    model = Servant
    template_name = "fgo_master_app/servant.html"


class CraftEssenceView(TemplateView):
    template_name = "fgo_master_app/craft-essence.html"


class CommandCodeView(TemplateView):
    template_name = "fgo_master_app/command-code.html"


class MysticCodeView(TemplateView):
    template_name = "fgo_master_app/mystic-code.html"
