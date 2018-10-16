from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class TopMenuView(TemplateView):
    template_name = "fgo_master_app/top-menu.html"
