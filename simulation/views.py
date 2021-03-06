import os

from django.core.files import File
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from simulation.models import SimulationModel
from simulation.serializers import SimulationModelInputSerializer, SimulationModelResultsSerializer
from simulator.exemple_queueing import Simulator


class SimulationsView(APIView):

    def post(self, request):
        serializer = SimulationModelInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        simulation = serializer.save()
        simulator = Simulator(simulation)
        simulator.simulate()

        return Response(data=simulation.id, status=status.HTTP_201_CREATED)


class SimulationView(APIView):
    def get(self, request, id_simulation):
        simulation = get_object_or_404(SimulationModel, id=id_simulation)
        serializer = SimulationModelResultsSerializer(simulation)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DownloadSimulationView(APIView):
    def get(self, request, id_simulation):
        path_to_file = os.path.realpath(f'Compressed{id_simulation}.tar')
        f = open(path_to_file, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/gzip')
        response['Content-Disposition'] = f'attachment; filename=Compressed{id_simulation}.tar.gz'
        return response
