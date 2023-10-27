from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class WallTemplate(TemplateView):
    template_name = 'main.html'
