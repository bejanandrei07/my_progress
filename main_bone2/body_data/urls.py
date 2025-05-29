from django.urls import path, include

import body_data
from body_data import views
from body_data.views import Createbody_data, Createbody_data2

#from main_bone2.urls import urlpatterns

app_name = "body_data"
urlpatterns = [
    path("", Createbody_data2.as_view(), name ="add_mesure")
]