from django.contrib.postgres.fields import ArrayField
from django.db import models


class SimulationModel(models.Model):
    sigma_PG = models.DecimalField(max_digits=7, decimal_places=5)
    sigma_MG = models.DecimalField(max_digits=7, decimal_places=5)
    sigma_S = models.DecimalField(max_digits=7, decimal_places=5)
    mean_PG = models.DecimalField(max_digits=7, decimal_places=5)
    mean_MG = models.DecimalField(max_digits=7, decimal_places=5)
    mean_S = models.DecimalField(max_digits=7, decimal_places=5)
    alpha_A = models.DecimalField(max_digits=7, decimal_places=5)
    beta_A = models.DecimalField(max_digits=7, decimal_places=5)
    n_cranes = models.IntegerField()
    max_time = models.IntegerField()
    mean_time = models.DecimalField(max_digits=7, decimal_places=5)
    percent_trucks_in_queue = models.DecimalField(max_digits=7, decimal_places=5)
    max_time_in_queue = models.IntegerField()
    n_trucks_in_queue = ArrayField(ArrayField(models.IntegerField()))