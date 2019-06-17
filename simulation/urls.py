from django.conf.urls import url
from django.urls import path, include

from simulation import views

urlpatterns = [
    url(r'^$', views.SimulationsView.as_view()),
    path('<id_simulation>', views.SimulationView.as_view()),
    path('download/<id_simulation>', views.DownloadSimulationView.as_view()),
]