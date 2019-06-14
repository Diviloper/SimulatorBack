from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from simulation.models import SimulationModel
from simulation.serializers import SimulationModelInputSerializer, SimulationModelResultsSerializer
#from simulator.exemple_queueing import Simulator


class SimulationsView(APIView):

    def post(self, request):
        serializer = SimulationModelInputSerializer(data=request.data)
        serializer.is_valid()
        simulation = serializer.save()
       # simulator = Simulator(simulation)
        #simulator.simulate()

        return Response(data=simulation.id, status=status.HTTP_201_CREATED)


class SimulationView(APIView):
    def get(self, request, id_simulation):
        simulation = get_object_or_404(SimulationModel, id=id_simulation)
        serialized = SimulationModelResultsSerializer(simulation)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
