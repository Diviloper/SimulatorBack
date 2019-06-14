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
    mean_time = models.DecimalField(max_digits=100, decimal_places=5, null=True, blank=True, default=0)
    percent_trucks_in_queue = models.DecimalField(max_digits=100, decimal_places=5, null=True, blank=True, default=0)
    max_time_in_queue = models.IntegerField(null=True, blank=True, default=0)
    n_trucks_in_queue = models.TextField()
