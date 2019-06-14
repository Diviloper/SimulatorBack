class Truck:

    def __init__(self, truck_id):
        self.id = truck_id
        self.asc = -1
        self.crane = -1
        self.waited_time = 0

    def start_waiting_time(self, current_time):
        self.waited_time = - current_time

    def finish_waiting(self, current_time, simulator):
        self.waited_time += current_time
        simulator.waited_time_for_truck.append(self.waited_time)

