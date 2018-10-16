from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class TopMenuView(TemplateView):
    template_name = "fgo_master_app/top-menu.html"


class CardDataView(TemplateView):
    template_name = "fgo_master_app/card-data.html"


class SynthesisSchemeView(TemplateView):
    template_name = "fgo_master_app/synthesis-scheme.html"


class BattleSimulatorView(TemplateView):
    template_name = "fgo_master_app/battle-simulation.html"
