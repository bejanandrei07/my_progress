from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from body_data.models import Measurements


# Create your views here.
class ProgressListView(ListView):
    model = Measurements
    template_name = 'view_progress/progress.html'
    context_object_name = 'entries'
    ordering = ['-date_add']


class HomePageView(TemplateView):
    template_name = "view_progress/home.html"