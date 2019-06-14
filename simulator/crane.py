import queue


class Crane:

    def __init__(self):
        self.slots = 1
        self.num_trucks = 0
        self.queue = queue.Queue()
        self.queue_evolution = []

    def free_crane(self):
        return self.slots > self.num_trucks

    def in_truck(self, truck, current_time):
        if self.free_crane():
            self.num_trucks += 1
            return True
        else:
            self.queue.put(truck)
            truck.start_waiting_time(current_time)
            return False

    def finished(self, current_time, simulator):
        if self.queue.empty():
            self.num_trucks -= 1
            return None
        else:
            in_truck = self.queue.get()
            in_truck.finish_waiting(current_time, simulator)
            return in_truck
