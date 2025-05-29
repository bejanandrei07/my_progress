from audioop import reverse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from body_data.forms import MeasurementsForms
from body_data.models import Measurements


# Create your views here.



class Createbody_data2(CreateView):
    model = Measurements
    form_class = MeasurementsForms
    template_name = "body_data/form.html"
    success_url = reverse_lazy('view_progress:progresslist')

    def form_valid(self, form):
        print("🧪 Cleaned data from form:")
        for key, value in form.cleaned_data.items():
            print(f"{key}: {value}")
        return super().form_valid(form)


class Createbody_data(ListView):
    model = Measurements
    template_name = "body_data/body.html"
    context_object_name = 'bodys'