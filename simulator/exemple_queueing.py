import json
import queue
import numpy as np
from decimal import Decimal

from simulator.crane import Crane
from simulator.event import *


class Simulator:

    def __init__(self, simulation) -> None:
        super().__init__()
        self.simulation = simulation
        np.random.seed(self.simulation.seed)
        self.cranes = [Crane() for _ in range(self.simulation.n_cranes)]
        self.waited_time_for_truck = []
        self.truck_counter = 0

    def simulate(self):
        cua = queue.PriorityQueue()
        cua.put(Arrival.generate(0.0, Truck(0), self))
        current_time = 0.0
        max_time = 84400.0
        while current_time < max_time:
            current_event = cua.get()
            current_time = current_event[0]
            for event in current_event[1].generate_next(current_time):
                cua.put(event)
            print(current_event)
        queue_matrix = np.zeros((self.simulation.n_cranes, 24 * 60), dtype=np.int)
        total_trucks_in_queue = np.zeros((1, 24 * 60), dtype=np.int)
        for index in range(self.simulation.n_cranes):
            previous_event_time = 0
            for event in self.cranes[index].queue_evolution:
                minute = int(event[0] / 60)
                value = event[1]
                if value:
                    queue_matrix[index][minute] = queue_matrix[index][previous_event_time] + 1
                else:
                    queue_matrix[index][minute] = queue_matrix[index][previous_event_time] - 1
                for m in range(previous_event_time, minute):
                    queue_matrix[index][m] = queue_matrix[index][previous_event_time]
                previous_event_time = minute
            for m in range(previous_event_time, 24 * 60):
                queue_matrix[index][m] = queue_matrix[index][previous_event_time]
        for i in range(24):
            for j in range(24 * 60):
                total_trucks_in_queue[0][j] += queue_matrix[i][j]
        collapsed_matrix = np.zeros((self.simulation.n_cranes, 24), dtype=np.int)
        for crane in range(self.simulation.n_cranes):
            for i in range(24):
                suma = 0
                for j in range(60):
                    index = i*24 + j
                    suma += queue_matrix[crane][index]
                collapsed_matrix[crane][i] = (suma // 60)

        self.simulation.mean_time = Decimal(sum(self.waited_time_for_truck) / len(self.waited_time_for_truck))
        self.simulation.percent_trucks_in_queue = (len(self.waited_time_for_truck) * 100) // self.truck_counter
        self.simulation.max_time_in_queue = Decimal(max(self.waited_time_for_truck))
        self.simulation.n_trucks_in_queue = json.dumps(collapsed_matrix.tolist())
        self.simulation.save()

        np.savetxt('Queues.csv', queue_matrix, delimiter=';', fmt='%i')
        np.savetxt('TotalWaitingTrucks.csv', total_trucks_in_queue, delimiter=';', fmt='%i')
        np.savetxt('WaitedTimeInQueue.csv', self.waited_time_for_truck, delimiter=';', fmt='%i')
