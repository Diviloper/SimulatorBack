from rest_framework import serializers
from simulation.models import SimulationModel


class SimulationModelInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationModel
        fields = ('sigma_PG', 'sigma_MG', 'sigma_S', 'mean_PG', 'mean_MG', 'mean_S',
                  'alpha_A', 'beta_A', 'n_cranes', 'seed')


class SimulationModelResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationModel
        fields = ('mean_time', 'percent_trucks_in_queue', 'max_time_in_queue', 'n_trucks_in_queue')
