# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Servant

# Create your views here.


# ルート階層
class TopMenuView(TemplateView):

    template_name = "fgo_master_app/top-menu.html"


# TopMenu階層
class SpiritOriginView(TemplateView):

    template_name = "fgo_master_app/spirit-origin.html"


class SynthesisSchemeView(TemplateView):

    template_name = "fgo_master_app/synthesis-scheme.html"


class BattleSimulatorView(TemplateView):

    template_name = "fgo_master_app/battle-simulation.html"


# SpiritOrigin階層
class ServantView(ListView):

    queryset = Servant.objects.order_by('No')
    context_object_name = "servants_list"
    template_name = "fgo_master_app/servant.html"
    paginate_by = 20


class CraftEssenceView(TemplateView):

    template_name = "fgo_master_app/craft-essence.html"


class CommandCodeView(TemplateView):

    template_name = "fgo_master_app/command-code.html"


class MysticCodeView(TemplateView):

    template_name = "fgo_master_app/mystic-code.html"


# Servant階層
class ServantDetailView(DetailView):

    model = Servant
    template_name = "fgo_master_app/servant-detail.html"
    slug_field = "No"
