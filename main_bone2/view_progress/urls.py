from django.urls import path

import view_progress
from body_data.urls import app_name, urlpatterns
from .views import ProgressListView

app_name = 'view_progress'

urlpatterns = [
    path("", ProgressListView.as_view(), name = 'progresslist')
]